import cv2
import numpy as np

cv2.namedWindow("IMAGE",cv2.WINDOW_NORMAL)

img = cv2.imread("flash.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

# Aspect Ratio
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

# 2. Extent
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

# 3. Solidity

area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

# 4. Equivalent Diameter

area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# 5. Orientation

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

# 6. Mask and Pixel Points

mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)

# 7. Maximum Value, Minimum Value and their locations

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)

# 8. Mean Color or Mean Intensity
mean_val = cv2.mean(im,mask = mask)

# 9. Extreme Points

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

cv2.imshow("IMAGE",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
