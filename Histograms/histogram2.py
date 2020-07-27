import cv2
import numpy as np

cv2.namedWindow("Hist",cv2.WINDOW_NORMAL)

img = cv2.imread('histo.jpg',0)

equ = cv2.equalizeHist(img)

res = np.hstack((img,equ))

cv2.imwrite("Results/result.jpg",res)

cv2.imshow("Hist",res)



cv2.waitKey(0)
cv2.destroyAllWindows()
