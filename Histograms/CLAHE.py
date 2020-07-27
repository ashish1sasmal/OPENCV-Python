import cv2
import numpy as np
import time

cv2.namedWindow("Hist",cv2.WINDOW_NORMAL)

img = cv2.imread('histo2.jpg',0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite("Results/CLAHE_result.jpg",cl1)


time.sleep(2.0)
cv2.imshow("Hist",cl1)



cv2.waitKey(0)
cv2.destroyAllWindows()
