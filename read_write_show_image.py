import cv2
img=cv2.imread('dan.jpg',-1)  # imread --> read the image
						 # ('path to image',flag=1(color) or
						 # 0(grayscale) or -1(alpha channel))

print(img)  # img stores a matrix

cv2.imshow('image',img)  # imshow()  --> display the image
						 # ('name of window' ,variable value(matrix form))

k = cv2.waitKey(0)		#  waitkey()  --> time limit of image displayed
						# key value get stored in k variable

if k==27:				# if the key is 'ESC' button
	cv2.destroyAllWindows()
elif ord('s'):           #if ctrl+s is pressed

	cv2.imwrite('dan_copy.png',img)
	cv2.destroyAllWindows()
