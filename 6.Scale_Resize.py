import cv2
from cv2 import imshow
import os

RTSP_URL = 'rtsp://user:Mubeausa@10.65.68.125:8554/streaming/channels/0601'
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
 
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
	print('Cannot open RTSP stream')
	exit(-1)
 
while True:
	#Load our input image
	_, frame = cap.read()
	
	#make it 75% of original image
	scaled_image = cv2.resize(frame, None,fx=0.50,fy=0.50)
	# show the image
	#-imshow("Scaled 75%", scaled_image)
	# double the size of the image
	scaled_image = cv2.resize(frame,None, fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
	imshow("Scaled 200%", scaled_image)
	


	if cv2.waitKey(1) == 27: #escape key
		break
 
cap.release()
cv2.destroyAllWindows()