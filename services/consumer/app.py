import pika
import logging
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASSWORD)
    ))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)

    def on_message(ch, method, properties, body):
        logging.error('Received message: {message}'.format(message=body))
        channel.basic_ack(method.delivery_tag)

    channel.queue_declare(queue='test', durable=True, exclusive=False, auto_delete=False, arguments={'x-queue-type': 'stream'})
    channel.basic_consume(queue='test', on_message_callback=on_message, auto_ack=False)

    channel.start_consuming()


if __name__ == '__main__':
    main()
