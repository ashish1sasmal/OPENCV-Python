import cv2
import numpy as np
from live_cam import live
cap = cv2.VideoCapture(0)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Laplacian', cv2.WINDOW_NORMAL)
cv2.namedWindow('SobelX', cv2.WINDOW_NORMAL)
cv2.namedWindow('SobelY', cv2.WINDOW_NORMAL)


while(1):

    # _, frame = cap.read()
    img=live()
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    cv2.imshow('Original',img)
    cv2.imshow('Laplacian',laplacian)
    cv2.imshow("SobelX",sobelx)
    cv2.imshow("SobelY",sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
