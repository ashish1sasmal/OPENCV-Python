import cv2
import numpy as np

def nothing():
    pass

img = cv2.imread("dan.jpg")
ret, thres = cv2.threshold(img,1,255,cv2.THRESH_BINARY)
# ret, thres = cv2.threshold(img,1,255,cv2.THRESH_BINARY_INV)
# ret, thres = cv2.threshold(img,1,255,cv2.THRESH_TRUNC)
# ret, thres = cv2.threshold(img,1,255,cv2.THRESH_TOZERO)
# ret, thres = cv2.threshold(img,1,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Image",thres)
cv2.createTrackbar('Contrast','Image',1,255,nothing)

while (1):
    cv2.imshow("Image",thres)

    cont = cv2.getTrackbarPos('Contrast','Image')
    ret, thres = cv2.threshold(img,cont,255,cv2.THRESH_BINARY)
    # ret, thres = cv2.threshold(img,cont,255,cv2.THRESH_BINARY_INV)
    # ret, thres = cv2.threshold(img,cont,255,cv2.THRESH_TRUNC)
    # ret, thres = cv2.threshold(img,cont,255,cv2.THRESH_TOZERO)
    # ret, thres = cv2.threshold(img,cont,255,cv2.THRESH_TOZERO_INV)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
