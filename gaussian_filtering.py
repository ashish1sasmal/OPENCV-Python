# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# def nothing():
#     pass
#
# cv2.namedWindow('GaussianBlur', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Averaging', cv2.WINDOW_NORMAL)
# cv2.namedWindow('MedianBlur', cv2.WINDOW_NORMAL)
#
# img = cv2.imread("mona.png")
# cv2.imshow("GaussianBlur",img)
# cv2.imshow("Averaging",img)
# cv2.imshow("MedianBlur",img)
#
# cv2.createTrackbar('Blur','GaussianBlur',1,100,nothing)
#
# while (1):
#
#     b =  cv2.getTrackbarPos('Blur','GaussianBlur')
#
#     if b>0:
#         dst1 = cv2.GaussianBlur(img,(2*(b//2)+1,2*(b//2)+1),0)
#
#         dst2 = cv2.blur(img,(b,b))
#         dst3 = cv2.medianBlur(img,2*(b//2)+1)
#         cv2.imshow('GaussianBlur',dst1)
#         cv2.imshow('Averaging',dst2)
#         cv2.imshow('MedianBlur',dst3)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()


import cv2
import numpy as np
from live_cam import live
cap = cv2.VideoCapture(0)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Averaging', cv2.WINDOW_NORMAL)
cv2.namedWindow('GaussianBlur', cv2.WINDOW_NORMAL)
cv2.namedWindow('MedianBlur', cv2.WINDOW_NORMAL)


while(1):

    # _, frame = cap.read()
    frame=live()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    dst1 = cv2.GaussianBlur(res,(5,5),0)

    dst3 = cv2.medianBlur(res,5)
    cv2.imshow('Original',frame)
    cv2.imshow('Averaging',smoothed)
    cv2.imshow("GaussianBlur",dst1)
    cv2.imshow("MedianBlur",dst3)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
