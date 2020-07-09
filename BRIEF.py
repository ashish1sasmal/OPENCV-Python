# Binary Robust Independent Elementary Features

import cv2
import numpy as np


cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

img = cv2.imread("cheetah.jpg",0)
# Initiate STAR detector (CenSurE detector is called STAR detector in OpenCV)
star = cv2.xfeatures2d.StarDetector_create()

# Initiate BRIEF extractor

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# find the keypoints with STAR
kp = star.detect(img,None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

img=cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
print(des.shape)
