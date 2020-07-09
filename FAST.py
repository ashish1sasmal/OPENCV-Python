# FEATURES from ACCELERATED SIMULATION TEST

import cv2
import numpy as np

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

img = cv2.imread("butterfly2.jpg",0)

fast = cv2.FastFeatureDetector_create(100)

kp = fast.detect(img,None)

img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0))

cv2.imshow("Image",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
