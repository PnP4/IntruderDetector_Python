#sudo apt-get install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip
#sudo pip install https://github.com/sightmachine/SimpleCV/zipball/develop
#sudo pip install svgwrite
import base64
import time

import __init__
import json


for i in range(0,10):
    image_64_decode = base64.decodestring(__init__.get_image())
    image_result = open('deer_decode'+str(i)+'.png', 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)

while True:
    try:
        while True:
            print 1
            data = json.loads(__init__.socket.recv())
            if (data["To"] == 3):
                filter(data)

    except Exception, e:
        print e