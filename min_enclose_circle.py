import cv2
import numpy as np

cv2.namedWindow("IMAGE",cv2.WINDOW_NORMAL)

img = cv2.imread("flash.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)


cv2.imshow("IMAGE",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
