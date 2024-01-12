# python manage.py runscript match_worker

import json
import pika
import requests
from rapidfuzz import fuzz

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='match_queue', durable=True)
channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch, method, properties, body):
    task_message = json.loads(body)

    response = requests.get('http://127.0.0.1:7000/api/v1/addresses/')
    addresses = [a_address['address'] for a_address in response.json()]

    top_score = 0
    min_score = 70
    match_address = task_message["address"]
    for base_address in addresses:
        score = round(fuzz.ratio(task_message["address"].lower(), str(base_address).lower()))
        if score >= top_score and score >= min_score:
            top_score = score
            match_address = base_address
        if top_score == 100:
            continue

    print(f'Match address: {match_address} > Score: {top_score}')

    address = {"name": task_message["name"],
               "address": match_address,
               "postalcode": task_message["postalcode"],
               "city": task_message["city"],
               "country": task_message["country"],
               "email": task_message["email"]
               }

    response = requests.post('http://127.0.0.1:7000/api/v1/addresses/', data=address)

    print("New subscription added for", task_message["name"])

    channel.basic_publish(exchange='',
                          routing_key='mail_queue',
                          body=json.dumps(task_message),
                          properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
                          )

    ch.basic_ack(delivery_tag=method.delivery_tag)


def run():
    print("Waiting for match address requests")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='match_queue', on_message_callback=callback)

    channel.start_consuming()
