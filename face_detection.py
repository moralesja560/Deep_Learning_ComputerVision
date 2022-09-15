
import cv2
import numpy as np
from cv2 import imshow
import sys 
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def empty(a):
	pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",(800,240))
cv2.createTrackbar("scaleFactor","Trackbars",20,30,empty)
cv2.createTrackbar("minNeighbors","Trackbars",1,7,empty)
cv2.createTrackbar("scaleFactor_eye","Trackbars",20,30,empty)
cv2.createTrackbar("minNeighbors_eye","Trackbars",1,7,empty)


face_classifier = cv2.CascadeClassifier(resource_path('images/haarcascade_frontalface_default.xml'))
eye_classifier = cv2.CascadeClassifier(resource_path('images/haarcascade_eye.xml'))


cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)


while True:
	#Load our input image
	_, frame = cap.read()
	sc_f = cv2.getTrackbarPos("scaleFactor","Trackbars")/10
	min_n = cv2.getTrackbarPos("minNeighbors","Trackbars")
	sc_f_eye = cv2.getTrackbarPos("scaleFactor","Trackbars")/10
	min_n_eye = cv2.getTrackbarPos("minNeighbors","Trackbars")
	if sc_f <1.1:
		sc_f = 1.1

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray, scaleFactor=sc_f, minNeighbors=min_n)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(127,0,255),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_classifier.detectMultiScale(roi_gray,sc_f_eye,min_n_eye)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
	imshow('face',frame)

	if cv2.waitKey(1) == 27: #escape key
		break

cap.release()
cv2.destroyAllWindows()
