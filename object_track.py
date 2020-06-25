import cv2
import urllib.request
import numpy as np

url='http://192.168.43.1:8080/shot.jpg'

cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    frame = cv2.resize(frame,(720,720))
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([50,100,100])
    upper_blue = np.array([70,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    mask = cv2.resize(mask,(500,500))
    res = cv2.resize(res,(500,500))

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
