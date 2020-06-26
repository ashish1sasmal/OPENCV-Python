import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing():
    pass

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)


img = cv2.imread("white_noise.jpg")
cv2.imshow("Image",img)


cv2.createTrackbar('Erosion','Image',1,100,nothing)

while (1):

    b =  cv2.getTrackbarPos('Erosion','Image')

    kernel = np.ones((b,b), np.uint8)
    ers = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    cv2.imshow('Image',ers)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
