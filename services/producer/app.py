import time
import pika
import logging
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD


logging.getLogger().setLevel('INFO')


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASSWORD)
    ))
    channel = connection.channel()
    channel.queue_declare(queue='test', durable=True, exclusive=False, auto_delete=False, arguments={'x-queue-type': 'stream'})

    while True:
        logging.info('Sending message')
        message = 'Hello, world'.encode('utf-8')
        channel.basic_publish(exchange='', routing_key='test', body=message)
        time.sleep(5)


if __name__ == '__main__':
    main()
