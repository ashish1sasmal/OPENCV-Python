import cv2
import numpy as np
import matplotlib.pyplot as plt

#
# cv2.namedWindow("TM",cv2.WINDOW_NORMAL)
img = cv2.imread("Brain Tumors/tumor2.jpg",0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img = clahe.apply(img)
templ = cv2.imread("Brain Tumors/test_brain.png",0)
templ = clahe.apply(templ)
print(50/templ.shape[::-1][0], 64/templ.shape[::-1][1])
templ = templ[74:138, 70:120]

templ = cv2.resize(templ,(0,0), fx=(img.shape[::-1][0]*50)/templ.shape[::-1][0] , fy=(img.shape[::-1][1]*64)/templ.shape[::-1][1])

w, h =templ.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

out = img.copy()

method = eval(methods[0])
res  = cv2.matchTemplate(out, templ, method)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print(min_val, max_val, min_loc, max_loc)

top_left = max_loc
print(top_left)
bottom_right = (max_loc[0]+w, max_loc[1]+h)

cv2.rectangle(out, top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(methods[0])
plt.show()

# 70, 74
# 120, 138
