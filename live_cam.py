import urllib.request
import cv2
import numpy as np


# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.43.1:8080/shot.jpg'

def live():

    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    return img
