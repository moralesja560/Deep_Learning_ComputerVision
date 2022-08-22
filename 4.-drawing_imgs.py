import cv2 
import numpy as np
from matplotlib import pyplot as plt


#draw a black image

while True:
	# a black image
	image = np.zeros((800,800,3),np.uint8)
	# a grayscale image without the depth
	gray_image = np.zeros((800,800),np.uint8)

	#draw a diagonal line
	cv2.line(image,(0,0),(800,800),(255,0,0),10)
	#draw a rectangle
	cv2.rectangle(image,(5,5),(795,795),(0,255,0),5)
	#draw a circle
	cv2.circle(image,(400,400),100,(0,0,255),-1)
	#draw a polygon
		#define points X then Y from upper left
	pts = np.array([[400,100],[685,307],[576,642],[223,642],[114,307]],np.int32)
	#print(f" ndim: {pts.ndim}")
	#print(f" shape: {pts.shape}")
	#print(f" array: {pts}")
	#print(f" example: {pts[0]}")q
	pts.reshape((-1,1,2))
	#print(f" ndim: {pts.ndim}")
	#print(f" shape: {pts.shape}")
	#print(f" array: {pts}")
	#print(f" example: {pts[0]}")
	cv2.polylines(image,[pts],True,(0,200,255),3)

	#put some text
	ourString =  'Hello World!'
	cv2.putText(image, ourString, (155,290),cv2.FONT_HERSHEY_COMPLEX,fontScale=3,color=(40,150,52),thickness=4)

	cv2.imshow("Black Canvas - RGB Color", image)
	cv2.imshow("Black Canvas - Grayscale", gray_image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


