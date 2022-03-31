import pika


class RabbitMQApi:
    def __init__(self, host: str, port: int, user: str, password: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def start_consuming(self, on_message_callback):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=pika.PlainCredentials(username=self.user, password=self.password)
        ))
        channel = connection.channel()
        channel.basic_qos(prefetch_count=1)

        def on_message(ch, method, properties, body):
            on_message_callback(body)
            channel.basic_ack(method.delivery_tag)

        channel.queue_declare(queue='test', durable=True, exclusive=False, auto_delete=False,
                              arguments={'x-queue-type': 'stream'})
        channel.basic_consume(queue='test', on_message_callback=on_message, auto_ack=False)

        channel.start_consuming()
