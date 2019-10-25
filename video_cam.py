import cv2

cap=cv2.VideoCapture(0) 			# (mode)  mode --> 0 or -1 values for camera
											# 'filename.ext'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:									# loop till true
	ret,frame=cap.read()					# ret --> true or false
	if ret ==True:										#frame= captures frame through camera
		out.write(frame)
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)		# convert colors
		cv2.imshow('video',gray)				# display video via camera

		if cv2.waitKey(1) & 0xFF ==ord('q'):
			break


cap.release()								# release captured content
out.release()
cv2.destroyAllWindows()
