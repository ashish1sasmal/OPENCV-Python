import numpy as np
import cv2
from matplotlib import pyplot as plt
from live_cam import live

img1 = cv2.imread('cheetah.jpg',0)       # queryImage
img2 = cv2.imread('liveex.jpg',0) # trainImage

cv2.namedWindow('BFM', cv2.WINDOW_NORMAL)

orb = cv2.xfeatures2d.SIFT_create()
kp2, des2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher()
# Initiate SIFT detector


while True:

    img1 = live()
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)

    # create BFMatcher object


    # Match descriptors.
    matches = bf.knnMatch(des1,des2,k=2)

    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
    cv2.imshow("BFM",img3)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
