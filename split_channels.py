import cv2
import os,sys
import numpy as np


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



img = cv2.imread(resource_path(r"images\castara.jpeg"))



while True:
	#split image channels into separate images
	R,G,B = cv2.split(img)
	#show only the blue channel, it will look like a grayscale because it lacks the other channels.
	# I always thought that if i display only one channel, i would see a blueish image
	cv2.imshow("blue channel only",B)
	
	#create a matrix with zeroes to simulate empty R and G channels.
	# the :2 is to remove the last number that represents the depth of the array.
	zeroes = np.zeros(img.shape[:2],dtype="uint8")
	#
	cv2.imshow("Red channel", cv2.merge([zeroes,zeroes,R]))
	cv2.imshow("Green channel", cv2.merge([zeroes,G,zeroes]))
	cv2.imshow("Blue channel", cv2.merge([B,zeroes,zeroes]))
	#amplify a color 
	cv2.imshow("Blue channel+", cv2.merge([B+100,G,R]))
	#chahge to HSV from BGR
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	cv2.imshow("HSV colorspace", imgHSV)
	cv2.imshow("normal",img)
	#shot the HSV channels
	cv2.imshow("Hue",imgHSV[:,:,0])
	cv2.imshow("Sat",imgHSV[:,:,1])
	cv2.imshow("Value",imgHSV[:,:,2])
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
