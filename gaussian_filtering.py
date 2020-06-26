import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing():
    pass

cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
cv2.namedWindow('Image3', cv2.WINDOW_NORMAL)

img = cv2.imread("mona.png")
cv2.imshow("Image1",img)
cv2.imshow("Image2",img)
cv2.imshow("Image3",img)

cv2.createTrackbar('Blur','Image1',1,100,nothing)

while (1):

    b =  cv2.getTrackbarPos('Blur','Image1')

    if b>0:
        dst1 = cv2.GaussianBlur(img,(2*(b//2)+1,2*(b//2)+1),0)

        dst2 = cv2.blur(img,(b,b))
        dst3 = cv2.medianBlur(img,2*(b//2)+1)
        cv2.imshow('Image1',dst1)
        cv2.imshow('Image2',dst2)
        cv2.imshow('Image3',dst3)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
