import jwt
import logging
import os
import redis
import requests
from celery import shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv
from rapidfuzz import fuzz
from smtplib import SMTPException
from subscription.models import Address

logging.basicConfig(filename="logs.txt", filemode="w", format="%(asctime)s → %(name)s → %(levelname)s: %(message)s")

redis_client = redis.Redis(host='redis', port=6379, db=0)

load_dotenv()

jwt_key = os.getenv("JWT_KEY")
jwt_algorithms = os.getenv("JWT_ALGORITHMS")
expected_client_producer = os.getenv("CLIENT_PRODUCER")
expected_service_producer = os.getenv("SERVICE_PRODUCER")
service_token = os.getenv("SERVICE_TOKEN")


def decode_token(token: str, caller_type: str) -> dict:
    try:
        decoded_token = jwt.decode(jwt=token,
                                   key=jwt_key,
                                   algorithms=jwt_algorithms)
    except jwt.exceptions.InvalidSignatureError:
        match caller_type:
            case 'client':
                return {"client_producer": "The producer sent an invalid token"}
            case 'service':
                return {"service_producer": "The producer sent an invalid token"}
    return decoded_token


@shared_task
def match_address_task(address):
    calling_producer = decode_token(address['client_token'], 'client')['client_producer']
    if calling_producer == expected_client_producer:
        addresses = redis_client.lrange('addresses', 0, -1)  # read addresses from cache

        top_score = 0
        min_score = 70
        match_address = address["address"]
        for base_address in addresses:
            score = round(fuzz.ratio(address["address"].lower(), str(base_address.decode('utf-8')).lower()))
            if score >= top_score and score >= min_score:
                top_score = score
                match_address = base_address.decode('utf-8')
            if top_score == 100:
                continue

        print(f'Match address: {match_address} > Score: {top_score}')

        address = {"name": address["name"],
                   "address": match_address,
                   "postalcode": address["postalcode"],
                   "city": address["city"],
                   "country": address["country"],
                   "email": address["email"]
                   }
        print(address)

        response = requests.post('http://address-api:7000/api/v1/addresses/', data=address)
        redis_client.lpush('streets', match_address)  # add address to cache

        print(f"New address inserted for {address['name']}")

        send_email_task.delay(address["name"], address["address"], address["email"], service_token)
    else:
        print(f"Authentication failed (match_address_task): {calling_producer}")


@shared_task
def send_email_task(name: str, street: str, email: str, token: str) -> None:
    """
        This function is a Celery worker that sends (upon a 
        task request) a confirmation email to the provided 
        receiver. 
        To send the mail, it utilizes the Django send_mail 
        wrapper from the django.core.mail module. 

        Parameters:  
            name (string): name of the receiver  
            street (string): the address determined  
            email (string): email of the receiver 
            token (string): JWT token to authorize the calling 
                            producer 

        Globals:  
            Not applicable  

        Returns:  
            None 
    """
    try:
        calling_producer = decode_token(token, 'service')['service_producer']
        if calling_producer == expected_service_producer:
            send_mail(
                "Your subscription",
                f"Dear {name},\n\nThanks for subscribing to our magazine!\n\nWe registered the subscription at this address:\n{street}.\n\nAnd you'll receive the latest edition of our magazine within three days.\n\nCM Publishers",
                "magazine@cm-publishers.com",
                [email],
                fail_silently=False,
            )
        else:
            logging.error("Authentication failed")

    except SMTPException as e:
        logging.error(f"Sending email failed with this error: {e}")
    except:
        logging.error(f"Sending email failed.")
