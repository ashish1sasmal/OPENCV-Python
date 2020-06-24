import cv2
import numpy as np

path = 'dan.jpg'

img = cv2.imread(path)

kernel = np.ones((5,5),np.uint8)

image = cv2.erode(img, kernel, cv2.BORDER_REFLECT)
cv2.resize(image,(300,300))
# Displaying the image
cv2.imshow("window_name", image)



if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
