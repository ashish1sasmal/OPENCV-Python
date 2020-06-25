import cv2
import numpy as np

def nothing():
    pass

img = cv2.imread('app.jpg',1)
cv2.namedWindow("Scale", cv2.WINDOW_NORMAL)
res = cv2.resize(img,None,fx=0.1,fy=0.1,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Scale",res)
cv2.createTrackbar('Scale','Scale',1,10,nothing)



while (1):

    cv2.imshow("Scale",res)
    sc = cv2.getTrackbarPos('Scale','Scale')
    res = cv2.resize(img,None,fx=sc,fy=sc,interpolation = cv2.INTER_CUBIC)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
