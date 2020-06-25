import cv2

img = cv2.imread("dan.jpg")

cv2.imshow("Image",img)

temp = img[38:366, 611:895]


img[101:429,141:425]= temp

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
