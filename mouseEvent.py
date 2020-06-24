import cv2
import numpy as np


# ALL EVENTS IN CV2 pack
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        loc = f"{x}, {y}"
        cv2.putText(img,loc,(x,y),font,0.2,(0,255,0),1)
        cv2.imshow('Frame',img)


img = np.zeros((1280,720,3),np.uint8)
cv2.imshow('Frame',img)

cv2.setMouseCallback('Frame', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
