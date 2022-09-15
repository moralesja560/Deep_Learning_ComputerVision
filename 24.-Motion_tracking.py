import cv2
import numpy as np
from cv2 import imshow


cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

_, frame = cap.read()
	
width = int(cap.get(3))
height = int(cap.get(4))

#setup initial location of window
r,h,c,w = 250,90,200,125
track_window= (c,r,w,h)

#setup the ROI for tracking
roi =frame[r:r+h,c:c+w]
hsv_roi = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0.,70.,32.)),np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT,10,1)

while True:
	#Load our input image
	ret, frame = cap.read()

	if ret == True:
		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
		ret, track_window = cv2.meanShift(dst,track_window, term_crit)
		#ret, track_window = cv2.CamShift(dst,track_window,term_crit)
		x,y,w,h = track_window
		img2 = cv2.rectangle(frame, (x,y),(x+w,y+h),(255,255,255),2)
		imshow('Tracking',img2)

	if cv2.waitKey(1) == 27: #escape key
		break

cap.release()
cv2.destroyAllWindows()

