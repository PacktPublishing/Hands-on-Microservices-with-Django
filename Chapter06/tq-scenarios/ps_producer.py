import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='email', exchange_type='fanout')

for idx in range(1, 6):
    mail_task = {
        'name': f'M. McDoe{idx}',
        'email': f'mcdoe{idx}@yyz.com',
        'subject': 'Our Django offer',
        'body': 'Dear...'
    }

    channel.basic_publish(exchange='email',
                          routing_key='',
                          body=json.dumps(mail_task))

connection.close()
