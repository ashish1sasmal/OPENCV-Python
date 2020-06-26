import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing():
    pass

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)


img = cv2.imread("dan.jpg")

cv2.createTrackbar('Min','Image',1,1000,nothing)

cv2.createTrackbar('Max','Image',1,1000,nothing)

while (1):

    m =  cv2.getTrackbarPos('Min','Image')

    M =  cv2.getTrackbarPos('Max','Image')

    dst = cv2.Canny(img,m,M)
    cv2.imshow("Image",dst)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()