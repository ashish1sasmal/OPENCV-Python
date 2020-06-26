import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing():
    pass

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
img = cv2.imread("app.jpg")
cv2.imshow("Image",img)

cv2.createTrackbar('Blur','Image',1,100,nothing)


while (1):

    b =  cv2.getTrackbarPos('Blur','Image')
    dst = cv2.blur(img,(b,b))
    cv2.imshow('Image',dst)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
