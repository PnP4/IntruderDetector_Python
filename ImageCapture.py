#sudo apt-get install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip
#sudo pip install https://github.com/sightmachine/SimpleCV/zipball/develop
#sudo pip install svgwrite
import base64
import time
from SimpleCV import Camera
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




for i in range(0,10):
    image_64_decode = base64.decodestring(get_image())
    image_result = open('deer_decode'+str(i)+'.png', 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)
