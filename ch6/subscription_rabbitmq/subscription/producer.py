import json
import pika


# docker compose - multi-container
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
# single container
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='match_queue', durable=True)


def match_address_task_message(task_message):
    channel.basic_publish(exchange='',
                          routing_key='match_queue',
                          body=json.dumps(task_message),
                          properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
                          )
