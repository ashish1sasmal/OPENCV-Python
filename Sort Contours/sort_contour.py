import imutils
import cv2
import numpy as np

cv2.namedWindow("Sort",cv2.WINDOW_NORMAL)


def sort_contours(cnts,method='l-r'):
    reverse = False
    i=0
    if method == "r-l" or method == "b-t":
        reverse = True

    if method in ['t-b',b-t]:
        i=1

    boxes = [cv2.boundRect(c) for c in cnts]

    (cnts,boxes) = zip(*sorted(zip(cnts,boxes), key=lambda b:b[1][i], reverse = reverse))

    return (cnts,boxes)

def draw_contours(image,c,i):
    M = cv2.moments(c)
    cx = int(M['m01']/M['m00'])
    cy = int(M['m10']/M['m00'])

    cv2.putText(image,f"#{i+1}",(cx-20,cy),cv2.FONT_HERSHEY_PLAIN,2.0,(255,0,255),2)

    return image


image = cv2.imread("let.jpg")

accedge = np.zeros(image.shape[:2],dtype='uint8')

for channel in cv2.split(image):
    channel = cv2.medianBlur(channel,11)
    edge = cv2.Canny(channel,50,200)
    accedge = cv2.bitwise_or(accedge,edge)

cnts = cv2.findContours(accedge.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

orig = image.copy()

for (i,c) in enumerate(cnts):
    print(cv2.contourArea(c))
    image=draw_contours(image,c,i)

cv2.imshow("Sort",image)



cv2.waitKey(0)
cv2.destroyAllWindows()
