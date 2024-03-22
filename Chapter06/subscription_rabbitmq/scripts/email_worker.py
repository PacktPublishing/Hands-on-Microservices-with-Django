# python manage.py runscript email_worker

import json
import pika

from django.core.mail import send_mail

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch, method, properties, body):
    task_message = json.loads(body)

    send_mail(
        "Your subscription",
        f"Dear {task_message['name']},\n\nThanks for subscribing to our magazine! You'll receive the latest edition of our magazine within three days.\n\nCM Publishers",
        "magazine@cm-publishers.com",
        [task_message['email']],
        fail_silently=False,
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run():
    print("Waiting for email requests")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='mail_queue', on_message_callback=callback)

    channel.start_consuming()
