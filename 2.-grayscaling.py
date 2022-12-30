import cv2
import os,sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



img = cv2.imread(resource_path(r"images\castara.jpeg"))


while True:
	grayscale_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	cv2.imshow("grayscale",grayscale_img)
	cv2.imshow("normal",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
