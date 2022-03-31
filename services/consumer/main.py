import json
import logging
from rabbitmq.api import RabbitMQApi
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD


logging.getLogger().setLevel('INFO')


def on_message_callback(message_body):
    message_data = json.loads(message_body)
    logging.info('Received message: {message}'.format(message=message_data))


def main():
    listener = RabbitMQApi(host=RABBITMQ_HOST, port=RABBITMQ_PORT, user=RABBITMQ_USER, password=RABBITMQ_PASSWORD)
    listener.start_consuming(on_message_callback=on_message_callback)


if __name__ == '__main__':
    main()
