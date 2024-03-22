import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch, method, properties, body):
    mail_message = json.loads(body)
    print(f"Email sent to {mail_message['name']}")


channel.basic_consume(
    queue='mail_queue', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
