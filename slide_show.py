import os
import cv2
import time

e1 = cv2.getTickCount()

path = 'Harry/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

img1 = cv2.imread(files[1])
img1 = cv2.resize(img1,(1280,720))

cv2.imshow('Slide',img1)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)

cv2.waitKey(0)
cv2.destroyAllWindows()
