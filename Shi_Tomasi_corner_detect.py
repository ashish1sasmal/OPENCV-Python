import cv2
import numpy as np

import matplotlib.pyplot as plt

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

img = cv2.imread("chess.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,500,0.01,10)
corners = np.int0(corners)


for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(0, 0, 255),-1)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#
