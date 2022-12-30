#Object Tracking
import cv2
import numpy as np

# Initalize camera
#cap = cv2.VideoCapture(0)

# define range of color in HSV
lower = np.array([66,90,48])
upper = np.array([85,255,255])

# Create empty points array
points = []

# Get default camera window size

# Load video stream, long clip
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

# Get the height and width of the frame (required to be an interger)
width = int(cap.get(3)) 
height = int(cap.get(4))



ret, frame = cap.read()
Height, Width = frame.shape[:2]
frame_count = 0
radius = 0

while True:
  
	# Capture webcame frame
	ret, frame = cap.read()
	if ret:
		hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# Threshold the HSV image to get only green colors
		mask = cv2.inRange(hsv_img, lower, upper)
		#mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

		contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# Create empty centre array to store centroid center of mass
		center =   int(Height/2), int(Width/2)

		if len(contours) > 0:
		
			# Get the largest contour and its center 
			c = max(contours, key=cv2.contourArea)
			(x, y), radius = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)

			# Sometimes small contours of a point will cause a divison by zero error
			try:
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			except:
				center =   int(Height/2), int(Width/2)

			# Allow only countors that have a larger than 25 pixel radius
			if radius > 25:
			
				# Draw cirlce and leave the last center creating a trail
				cv2.circle(frame, (int(x), int(y)), int(radius),(0, 0, 255), 2)
				cv2.circle(frame, center, 5, (0, 255, 0), -1)

			# Log center points 
			points.append(center)

		# If radius large enough, we use 25 pixels
		if radius > 25:
		
			# loop over the set of tracked points
			for i in range(1, len(points)):
				try:
					cv2.line(frame, points[i - 1], points[i], (0, 255, 0), 2)
				except:
					pass

			# Make frame count zero
			frame_count = 0
		cv2.imshow('fff',frame)

	else:
		break
	if cv2.waitKey(1) == 27: #escape key
		break
# Release camera and close any open windows
cap.release()