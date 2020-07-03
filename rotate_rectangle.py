import cv2
import numpy as np

cv2.namedWindow("IMAGE",cv2.WINDOW_NORMAL)

img = cv2.imread("flash.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)

print(box)

box = np.int0(box)

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

img = cv2.drawContours(img,[box],0,(0,0,255),2)

cv2.imshow("IMAGE",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
