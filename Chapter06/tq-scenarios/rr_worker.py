import json
import pika
import random

from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='mail_queue', durable=True)


def on_request(ch, method, props, body):
    mail_message = json.loads(body)
    print(f"Email sent to {mail_message['name']}")

    response = "OK" if random.choice([True, False]) == True else "NOK"

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='mail_queue', on_message_callback=on_request)

channel.start_consuming()
