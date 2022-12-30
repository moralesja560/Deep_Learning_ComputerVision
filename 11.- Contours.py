import cv2
import numpy as np
from cv2 import imshow


cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)


while True:
	#Load our input image
	_, frame = cap.read()
	
	





	if cv2.waitKey(1) == 27: #escape key
		break

cap.release()
cv2.destroyAllWindows()
