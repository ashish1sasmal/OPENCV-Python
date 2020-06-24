import urllib.request
import cv2
import numpy as np
import time

from datetime import datetime

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.43.1:8080/shot.jpg'

while True:

    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # put the image on screen
    img = cv2.resize(img,(1280,720))
    font = cv2.FONT_HERSHEY_SIMPLEX

    img = cv2.putText(img, str(datetime.now()), (10,50),font,1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
