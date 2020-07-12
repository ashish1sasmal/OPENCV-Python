import cv2
import numpy as np

from live_cam import live

cv2.namedWindow("MOG",cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture("car2.mp4")


fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=20)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow("MOG",fgmask)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
