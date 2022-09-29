import json
import os

import models
import pika


def send_message_to_queue(link: models.Link) -> None:
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
    channel = connection.channel()
    channel.queue_declare(queue=os.environ['QUEUE_NAME'])
    channel.basic_publish(exchange='', routing_key=os.environ['QUEUE_NAME'], body=json.dumps({
        'id': link.id,
        'url': link.url
    }).encode('utf-8'))
    connection.close()
