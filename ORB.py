# Oriented FAST and Rotated Brief

import cv2
import numpy as np


cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

img = cv2.imread("build.jpg",0)

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0), flags=0)

cv2.imshow("ORB",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
