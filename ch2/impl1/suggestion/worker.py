import json
import pika

from django.core.mail import send_mail
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', credentials=pika.PlainCredentials("myuser", "mypassword")))
channel = connection.channel()

channel.queue_declare(queue='message_queue', durable=True)


def callback(ch, method, properties, body):
    message = json.loads(body)
    # sleep(10)
    print(f"Dear {message['name']}\n\nWe'll include your suggestion – {message['suggestion']} – into our improvement process.\n\nThanks for your contribution!\n\n------\n\n")

    send_mail(
        "Your suggestion",
        f"We'll include your suggestion – {message['suggestion']} – into our improvement process.\n\nThanks for your contribution!",
        "quality@xyz.com",
        [message['email']],
        fail_silently=False,
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='message_queue', on_message_callback=callback)

channel.start_consuming()
