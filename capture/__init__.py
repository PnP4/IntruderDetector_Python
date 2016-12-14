import json
import base64
from SimpleCV import Camera
from nanomsg import Socket, BUS

socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')


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
