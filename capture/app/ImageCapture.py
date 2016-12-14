#sudo apt-get install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip
#sudo pip install https://github.com/sightmachine/SimpleCV/zipball/develop
#sudo pip install svgwrite
import base64
import time

import capture
import json
import requests


for i in range(0,10):
    image_64_decode = base64.decodestring(capture.get_image())
    image_result = open('deer_decode'+str(i)+'.png', 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)




def callback(ch, method, properties, body):
    data = json.loads(body)
    channel.basic_publish(exchange='',
                          routing_key='detector',
                          body=json.dumps(data))

url = "http://192.168.1.4:4000"


def method(data):
    try:
        while True:

            datasend = {}

            r = requests.post(url, json=datasend)
            print r
            # print json.dumps(datasend)

    except Exception:
        print Exception.message