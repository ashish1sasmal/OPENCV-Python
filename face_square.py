import cv2

l=[]

def click_event(event,x,y,flags,param):
    global l
    # print(l)
    if event == cv2.EVENT_LBUTTONDOWN:
        l.append([x,y])
        if len(l) == 2:
            print(l)
            cv2.rectangle(img,(l[0][0],l[0][1]),(l[1][0],l[1][1]),(0,255,0),2)
            cv2.imshow('Frame',img)
            l=[]
       



img = cv2.imread("app.jpg")
cv2.imshow('Frame',img)

cv2.setMouseCallback('Frame', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
