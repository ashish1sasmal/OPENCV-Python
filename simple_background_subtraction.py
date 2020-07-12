import cv2
import numpy as np

cv2.namedWindow("Simple",cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture("car.mp4")

ret,first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
# Gaussian Blur

first_gray = cv2.GaussianBlur(first_gray, (5,5), 0)


while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    diff = cv2.absdiff(first_gray,gray)

    ret, diff  = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow("Simple",diff)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
