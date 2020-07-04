import cv2
import numpy as np

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

gray = cv2.imread('butterfly.jpg',0)

sift = cv2.xfeatures2d.SIFT_create()
kp,des = sift.detectAndCompute(gray,None)
print(des[0])
img=cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
