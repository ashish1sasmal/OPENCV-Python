import cv2

img = cv2.imread('dan.jpg',0)

img = cv2.line(img,(610,40), (880,40), (255,0,0),2)

							# cv2.line(img, (x1,y1), (x2,y2), (B,G,R), thickness)


img = cv2.arrowedLine(img,(0,0), (200,200), (255,0,0),2)

img=cv2.rectangle(img, (610,40), (880,370), (0,255,0) ,5)
												# coordinates of one diagonal
img=cv2.rectangle(img, (50,40), (80,90), (0,255,0) ,-1)																					#-1 value will fill the rect

img=cv2.circle(img,(60,460),40,(10,130,0),5)
											# center coordinates ,radius

font=cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Opencv', (10,400), font, 4, (0,255,255), 10, cv2.LINE_AA)

# (img, text , starting point, font_style, size, color, thick ,orientation)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
