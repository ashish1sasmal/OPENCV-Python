import cv2

cv2.namedWindow("LOC",cv2.WINDOW_NORMAL)

img = cv2.imread("Brain Tumors/test_brain.png")

cv2.imshow("LOC",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
