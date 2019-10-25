import cv2

cap=cv2.VideoCapture(0) 			# (mode)  mode --> 0 or -1 values for camera
											# 'filename.ext'

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,240)
cap.set(4,320)

print(cap.get(3))
print(cap.get(4))
while True:									# loop till true
	ret,frame=cap.read()					# ret --> true or false
	if ret ==True:										#frame= captures frame through camera
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)		# convert colors
		cv2.imshow('video',gray)				# display video via camera

		if cv2.waitKey(1) & 0xFF ==ord('q'):
			break


cap.release()								# release captured content

cv2.destroyAllWindows()
