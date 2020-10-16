# @Author: ASHISH SASMAL <ashish>
# @Date:   01-09-2020
# @Last modified by:   ashish
# @Last modified time: 16-10-2020



import cv2
import numpy as np

from live_cam import live

cv2.namedWindow("MOG",cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture("boy_ball.mp4")


fgbg = cv2.createBackgroundSubtractorMOG2(history=20)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    kernel = np.ones((4,4), np.uint8)
    ers = cv2.erode(fgmask,kernel,iterations=1)
    fgmask = cv2.resize(ers, (720,360))
    cv2.imshow("MOG",fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
