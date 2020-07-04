import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('chess.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)


corners = np.int0(corners)


for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 255, 0), -1)


cv2.imshow("imshow",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
