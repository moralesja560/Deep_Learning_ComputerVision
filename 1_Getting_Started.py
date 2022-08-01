import cv2
from matplotlib import pyplot as plt
import os,sys
import numpy as np


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


image = cv2.imread(resource_path(r"images\flowers.jpeg"))

#with pyplot
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

#with opencv
cv2.imshow("my first image",image)

print(image.shape,image.ndim)