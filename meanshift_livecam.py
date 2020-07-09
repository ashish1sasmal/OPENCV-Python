import numpy as np
import cv2
from live_cam import live


cv2.namedWindow("MeanShift",cv2.WINDOW_NORMAL)


# setup initial location of window
r,h,c,w = 0,872,0,813


img = cv2.imread("obj.jpg")

# cv2.rectangle(frame, (2467,1046), (2832,1296), (0,255,0),2)
#
# cv2.imshow("MeanShift",frame)
roi = img[r:r+h, c:c+w]

#
track_window = (c,r,w,h)

hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
        frame = live()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('MeanShift',img2)
        k = cv2.waitKey(200) & 0xff
        if k == 27:
            break



cv2.waitKey(0)
cv2.destroyAllWindows()
