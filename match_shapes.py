import cv2
import numpy as np
img = cv2.imread('b&w.jpg',0)

ret, thresh = cv2.threshold(img, 127, 255,0)


contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)
