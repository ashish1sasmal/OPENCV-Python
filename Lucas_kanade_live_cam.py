import cv2
import numpy as np
from live_cam import live

cv2.namedWindow("L-K",cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)

ret,frame = cap.read()

old_gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

lk_params = dict(winSize = (15,15),
                maxLevel = 4,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

def select_point(event,x,y,flags,params):
    global point,point_selected, old_points

    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        point_selected = True
        old_points = np.array([[x,y]], dtype=np.float32)

cv2.setMouseCallback("L-K",select_point)

point_selected = False
point = ()

old_points = np.array([[]])

while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if point_selected is True:
        cv2.circle(frame,point,5,(0,0,255),2)

        new_points,status,error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
        old_gray = gray_frame.copy()

        old_points = new_points

        x, y = new_points.ravel()
        cv2.circle(frame,(x,y),5,(0,255,0),-1)



    cv2.imshow("L-K",frame)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break



cv2.waitKey(0)
cv2.destroyAllWindows()
