import json
import base64
from SimpleCV import Camera
import pika


credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        '192.168.1.7',5672,'/', credentials ))

channel = connection.channel()
channel.queue_declare(queue='capture')
channel.queue_declare(queue='detector')


def checkistempincreased(temp):
    if(temp>100):
        return True;
    return False;

def get_image():
    cam = Camera()
    img = cam.getImage()
    img.save("filename.png")

    time.sleep(1)
    encoded = base64.b64encode(open("filename.png", "rb").read())
    return encoded
