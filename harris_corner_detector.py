import cv2
import numpy as np
from live_cam import live


# img = cv2.imread("cor.jpg")
cv2.namedWindow('Harris Corner', cv2.WINDOW_NORMAL)


while (1):

    img = live()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    dst = cv2.cornerHarris(gray,2,3,0.04)

    dst = cv2.dilate(dst,None)

    img[dst>0.01*dst.max()] = [0,0,255]

    cv2.imshow("Harris Corner",img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
