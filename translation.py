import cv2
import numpy as np

img = cv2.imread('app.jpg',1)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
print(img.shape[0:2])
rows, cols = img.shape[0:2]

M = np.float32([[1,0,300],[0,1,150]])

dst = cv2.warpAffine(img,M,(cols,rows))


cv2.imshow('output',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
