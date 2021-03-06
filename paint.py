# import cv2
# import numpy as np
#
# ix,iy = -1 ,-1
#
# def draw_circle(event,x,y,flags,param):
#     global ix,iy
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#
#         ix,iy = x,y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#
#         cv2.circle(img,(x,y),2,(0,0,255),-1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         cv2.circle(img,(x,y),2,(0,0,255),-1)
#
#
# img = np.zeros((300,512,3), np.uint8)
#
# cv2.namedWindow('Paint')
# cv2.setMouseCallback('Paint',draw_circle)
# def nothing(x):
#     pass
#
# cv2.createTrackbar('R','Paint',0,255,nothing)
# cv2.createTrackbar('G','Paint',0,255,nothing)
# cv2.createTrackbar('B','Paint',0,255,nothing)
#
# cv2.createTrackbar('Size','Paint',1,10,nothing)
#
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'Paint',0,1,nothing)
#
# while (True):
#     cv2.imshow('Paint',img)
#     k = cv2.waitKey(1) & 0xFF
#
#     if k==27:
#         break
#
#     r = cv2.getTrackbarPos('R','Paint')
#     g = cv2.getTrackbarPos('G','Paint')
#     b = cv2.getTrackbarPos('B','Paint')
#     sw = cv2.getTrackbarPos(switch,'Paint')
#     size = cv2.getTrackbarPos('Size','Paint')
#
#     if sw == 0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]


import cv2
import numpy as np

def nothing():
    pass

drawing =False
# true if mouse is pressed
mode =True
# if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

r,g,b = -1,-1,-1
size = 1


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,r,g,b
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing =True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing ==True:
            if mode ==True:
                cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            else:
                cv2.circle(img,(x,y),size,(b,g,r),-1)
    elif event == cv2.EVENT_LBUTTONUP:

        drawing =False
        if mode ==True:
            print('hello')
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r,),-1)
        else:
            cv2.circle(img,(x,y),size,(b,g,r),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint',draw_circle)

cv2.createTrackbar('R','Paint',0,255,nothing)
cv2.createTrackbar('G','Paint',0,255,nothing)
cv2.createTrackbar('B','Paint',0,255,nothing)

cv2.createTrackbar('Size','Paint',1,10,nothing)

while(1):
    cv2.imshow('Paint',img)

    r = cv2.getTrackbarPos('R','Paint')
    g = cv2.getTrackbarPos('G','Paint')
    b = cv2.getTrackbarPos('B','Paint')
    size = cv2.getTrackbarPos('Size','Paint')



    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode =not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
