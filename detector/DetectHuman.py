import numpy as np
import cv2
import base64
import __init__
import json


#image_64_decode = base64.decodestring("THE IMAGE BASE64STRING") #image string
#image_result = open('deer_decode.png', 'wb') # create a writable image and write the decoding result
#image_result.write(image_64_decode)



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('intruder.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print len(faces)

def callback(ch, method, properties, body):
    data = json.loads(body)


while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                           queue='detector',
                                           no_ack=True)

            __init__.channel.start_consuming()
    except Exception, e:
        print e

# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#     cv2.imshow('img',img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

