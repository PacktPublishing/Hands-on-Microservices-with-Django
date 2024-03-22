import requests
from celery import shared_task
from django.core.mail import send_mail
from rapidfuzz import fuzz
from subscription.models import Address


@shared_task
def match_address_task(address):
    response = requests.get('http://address-api:7000/api/v1/addresses/')
    addresses = [a_address['address'] for a_address in response.json()]

    top_score = 0
    min_score = 70
    match_address = address["address"]
    for base_address in addresses:
        score = round(fuzz.ratio(address["address"].lower(), str(base_address).lower()))
        if score >= top_score and score >= min_score:
            top_score = score
            match_address = base_address
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

    print(f"New address inserted for {address['name']}")

    send_email_task.delay(address["name"], address["address"], address["email"])


@shared_task
def send_email_task(name, street, email):
    send_mail(
        "Your subscription",
        f"Dear {name},\n\nThanks for subscribing to our magazine!\n\nWe registered the subscription at this address:\n{street}.\n\nAnd you'll receive the latest edition of our magazine within three days.\n\nCM Publishers",
        "magazine@cm-publishers.com",
        [email],
        fail_silently=False,
    )
