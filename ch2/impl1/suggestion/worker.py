import json
import pika

from django.core.mail import send_mail
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', credentials=pika.PlainCredentials("myuser", "mypassword")))
channel = connection.channel()

channel.queue_declare(queue='message_queue', durable=True)


def callback(ch, method, properties, body):
    task_message = json.loads(body)

    sleep(10)

    send_mail(
        "Your suggestion",
        f"We'll include your suggestion – {task_message['suggestion']} – into our improvement process.\n\nThanks for your contribution!",
        "quality@xyz.com",
        [task_message['email']],
        fail_silently=False,
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='message_queue', on_message_callback=callback)

channel.start_consuming()
