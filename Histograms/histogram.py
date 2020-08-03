# importing required libraries of opencv
import cv2
import numpy as np
# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('tumor4.jpg',0)
print(img.flatten())
mask = np.zeros(img.shape[:2], np.uint8)
mask[1294:1816, 1637:2107] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

hist_mask = cv2.calcHist([img],[0],None,[256],[0,256])


# show the plotting graph of an image
plt.plot(hist_mask)
plt.show()
