import cv2

l=[]

def click_event(event,x,y,flags,param):
    global l
    # print(l)
    if event == cv2.EVENT_LBUTTONDOWN:
        l.append([x,y])
        if len(l) == 3:
            print(l,l[2][0]+l[1][0]-l[0][0],l[2][1]+l[1][1]-l[0][1])
            img[l[2][1]:l[2][1]+l[1][1]-l[0][1], l[2][0]:l[2][0]+l[1][0]-l[0][0]] = img[l[0][1]:l[1][1], l[1][0]:l[1][0]]
            cv2.imshow('Frame',img)
            l=[]




img = cv2.imread("app.jpg")
cv2.imshow('Frame',img)

cv2.setMouseCallback('Frame', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
