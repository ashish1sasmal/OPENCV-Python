import cv2
import numpy as np

img1 = cv2.imread("dan.jpg")
img2 = cv2.imread("app.jpg")


img2 = cv2.resize(img2,img1.shape[0:2][::-1])

# img3 = cv2.addWeighted(img1,0.5,img2,0.3,0)
# cv2.imshow("wighted image",img3)

img4 = cv2.subtract(img1,0.5,img2,0.3,0)
cv2.imshow("wighted image",img4)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
