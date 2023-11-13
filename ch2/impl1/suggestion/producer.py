import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', credentials=pika.PlainCredentials("myuser", "mypassword")))
channel = connection.channel()

channel.queue_declare(queue='mail_queue', durable=True)


def send_email_message(message):
    channel.basic_publish(exchange='',
                          routing_key='mail_queue',
                          body=json.dumps(message),
                          properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
                          )
