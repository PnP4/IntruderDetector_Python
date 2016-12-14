import json
import pika


credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        '192.168.1.7',5672,'/', credentials ))

channel = connection.channel()
channel.queue_declare(queue='detector')