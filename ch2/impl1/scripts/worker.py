import json
import pika

from django.core.mail import send_mail
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', credentials=pika.PlainCredentials("myuser", "mypassword")))
channel = connection.channel()

channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch, method, properties, body):
    message = json.loads(body)

    sleep(10)

    send_mail(
        "Your suggestion for improving",
        f"We'll include your suggestion – {message['suggestion']} – into our improvement process.\n\nThanks for your contribution!",
        "quality@xyz.com",
        [message['email']],
        fail_silently=False,
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run():
    print("Waiting for email requests")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='mail_queue', on_message_callback=callback)

    channel.start_consuming()
