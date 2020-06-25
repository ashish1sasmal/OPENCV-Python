import cv2
import numpy as np
import matplotlib.pyplot as plt
#
# img = cv2.imread("dan.jpg")
# print(img.shape)
# rows,cols,ch = img.shape
#
# pts1 = np.float32([[183,91],[924,31],[934,454],[163,445]])
# pts2 = np.float32([[0,0],[960,0],[960,625],[0,625]])
#
# M = cv2.getPerspectiveTransform(pts1,pts2)
# dst = cv2.warpPerspective(img,M,(300,300))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

img = cv2.imread('dan.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[195,88],[897,54],[897,463],[186,442]])

pts2 = np.float32([[0,0],[960,0],[960,625],[0,625]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
