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
	_, frame = cap.read()
	
	imshow('Original Image',frame)
	#create our 3x3 kernel
	kernel_3x3 = np.ones((3,3),np.float32)/9
	blurred = cv2.filter2D(frame,-1,kernel_3x3)
	imshow('3x3', blurred)
	kernel_7x7 = np.ones((7,7),np.float32)/49
	blurred_7 = cv2.filter2D(frame,-1,kernel_7x7)
	imshow('blurred_7', blurred_7)
	if cv2.waitKey(1) == 27: #escape key
		break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

while True:
	#Load our input image
	_, frame = cap.read()
	bilateral = cv2.bilateralFilter(frame, 9, 75, 75)
	imshow('Bilateral Blurring', bilateral)
	imshow('Original Image',frame)
	dst = cv2.fastNlMeansDenoisingColored(frame,None,6,6,7,21)
	imshow('denoise', dst)

	if cv2.waitKey(1) == 27: #escape key
		break	

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

while True:
	#Load our input image
	_, frame = cap.read()
	kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
	sharpened = cv2.filter2D(frame,-1,kernel_sharpening)
	imshow('Sharpened image',sharpened)
	if cv2.waitKey(1) == 27: #escape key
		break	

cap.release()
cv2.destroyAllWindows()
