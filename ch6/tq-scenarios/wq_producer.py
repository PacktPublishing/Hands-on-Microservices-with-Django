import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='mail_queue', durable=True)

for idx in range(1, 6):
    mail_task = {
        'name': f'M. McDoe{idx}',
        'email': f'mcdoe{idx}@yyz.com',
        'subject': 'Our Django offer',
        'body': 'Dear...'
    }

    channel.basic_publish(exchange='',
                          routing_key='mail_queue',
                          body=json.dumps(mail_task),
                          properties=pika.BasicProperties(
                              delivery_mode=pika.DeliveryMode.Persistent))

connection.close()
