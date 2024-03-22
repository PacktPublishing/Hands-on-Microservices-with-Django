import json
import pika
import uuid


class Mailer(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, mail_task):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='mail_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(mail_task))
        self.connection.process_data_events(time_limit=None)
        return self.response


mail_task = {
    'name': f'M. McDoe',
    'email': f'mcdoe@yyz.com',
    'subject': 'Our Django offer',
    'body': 'Dear...'
}

mailer = Mailer()

response = mailer.call(mail_task)
print(response.decode('utf-8'))
