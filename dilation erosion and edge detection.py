import cv2
from cv2 import imshow
import os
import numpy as np

RTSP_URL = 'rtsp://user:Mubeausa@10.65.68.125:8554/streaming/channels/0601'
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
 
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

if not cap.isOpened():
	print('Cannot open RTSP stream')
	exit(-1)
 
while True:
	#Load our input image
	_, image = cap.read()
		
	#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# Let's define our kernel size
	kernel = np.ones((5,5), np.uint8)

	# Now we erode
	erosion = cv2.erode(image, kernel, iterations = 1)
	imshow('Erosion', erosion)

	# Dilate here
	dilation = cv2.dilate(image, kernel, iterations = 1)
	imshow('Dilation', dilation)

	# Opening - Good for removing noise
	opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
	imshow('Opening',opening)
	
	# Closing - Good for removing noise
	closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
	imshow('Closing',closing)

	canny = cv2.Canny(image, 50, 120)
	imshow('Canny 1', canny)

# Wide edge thresholds expect lots of edges
	canny = cv2.Canny(image, 10, 200)
	imshow('Canny Wide', canny)

# Narrow threshold, expect less edges 
	canny = cv2.Canny(image, 200, 240)
	imshow('Canny Narrow', canny)

	canny = cv2.Canny(image, 60, 110)
	imshow('Canny 4', canny)


	if cv2.waitKey(1) == 27: #escape key
		break

cap.release()
cv2.destroyAllWindows()