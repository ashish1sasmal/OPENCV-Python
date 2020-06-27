import cv2
import numpy as np
from live_cam import live

def nothing():
    pass

def contour(img):
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)

    image,contours= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    if len(image)>0:
        
        #moments
        cnt = image[0]
        M = cv2.moments(cnt)

        # Contour Area
        area = cv2.contourArea(cnt)
        print(area)

        # Contour perimeter
        peri = cv2.arcLength(cnt,True)
        print(peri)

        # Contour Approximation (Douglas-Peucker Algorithm)
        epsilon = 0.1*cv2.arcLength(cnt,True)
        image = cv2.approxPolyDP(cnt,epsilon,True)

    #drawing contours
    dst = cv2.drawContours(img,image,-1,(0,255,0), 3)

    return dst

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

# while (1):
#
#     img = live()
img = cv2.imread("3.jpg")
dst = contour(img)
print("Alright")
cv2.imshow("Image",dst)

cv2.imshow("Imag2",img)

cv2.waitKey(0)

# k = cv2.waitKey(1) & 0xFF
# if k == 27:
#     break

cv2.destroyAllWindows()
