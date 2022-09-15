import cv2
import numpy as np
from cv2 import imshow


cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

_, frame = cap.read()
	
width = int(cap.get(3))
height = int(cap.get(4))


feature_params = dict(maxCorners=1,qualityLevel=0.3,minDistance=7,blockSize=7)

lucas_kanade_params = dict(winSize = (15,15),maxLevel=2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT,10,0.03))

color = np.random.randint(0,255,(100,3))

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame,cv2.COLOR_BGR2GRAY)
prev_corners = cv2.goodFeaturesToTrack(prev_gray, mask = None, **feature_params)

#create a mask image for drawing purposes
mask = np.zeros_like(prev_frame)

while True:
	ret, frame = cap.read()

	if ret == True:
		frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		#calculate optical flow
		new_corners, status,errors = cv2.calcOpticalFlowPyrLK(prev_gray,frame_gray,prev_corners,None,**lucas_kanade_params)
		good_new = new_corners[status==1]
		good_old = prev_corners[status==1]

		#draw the tracks
		for i,(new,old) in enumerate(zip(good_new,good_old)):
			a,b = new.ravel()
			c,d = old.ravel()
			a=int(a)
			b=int(b)
			c=int(c)
			d=int(d)
			mask = cv2.line(mask,(a,b),(c,d),color[i].tolist(),2)
			frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
		img = cv2.add(frame,mask)
		imshow('Optical Flow - Lucas-Kanade',img)

		prev_gray = frame_gray.copy()
		prev_corners = good_new.reshape(-1,1,2)
		if cv2.waitKey(1) == 27: #escape key
			break

	else:
		break

cap.release()