import cv2
import numpy as np




img1 = cv2.imread('day.jpg',0)
img1 = img1/255

scale_percent = 60 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)




#cv2.imshow("image original", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)

pepper = 0.05
salt = 1 - pepper

#create salt and pepper noise image
for i in range(x):
	for j in range(y):
		rdn = np.random.random()
		if rdn < pepper:
			g[i][j] = 0
		elif rdn > salt:
			g[i][j] = 1
		else:
			g[i][j] = img[i][j]

#cv2.imwrite(r'C:\Users\SKU 80093\Documents\Python_Scripts\Deep_Learning_ComputerVision\day_salted10.jpg', g*255)

g2 = g.copy()

def median_filter(data, filter_size):
	data_after = data
	indexer = filter_size // 2
	# ancho*alto 3270*2716
	# ancho*alto 1962*1629
	# shape = alto*ancho
	ancho_img = range(0,data.shape[1])
	alto_img = range(0,data.shape[0])
	for pixel_alto in alto_img:
		for pixel_ancho in ancho_img:
			temp = []
			for z in range(filter_size):
				if pixel_alto + z - indexer < 0 or pixel_alto + z - indexer > len(data) - 1:
					for c in range(filter_size):
 						#temp.append(0)
						pass
				#else:
				#	if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
				#		temp.append(0)
				#	else:
				#		for k in range(filter_size):
				#			temp.append(data_after[i + z - indexer][j + k - indexer])
				else:
					for k in range(filter_size):
						if pixel_ancho + z - indexer < 0 or pixel_ancho + indexer > len(data[0]) - 1:
							temp.append(0)
						else:
							temp.append(data_after[pixel_alto + z - indexer][pixel_ancho + k - indexer])	

			temp.sort()
			data_after[pixel_alto][pixel_ancho] = temp[len(temp) // 2]

	return data_after

#img_median = cv2.medianBlur(g, 5)

img_median = median_filter(g,3)
while True:
	cv2.imshow("original", img)
	cv2.imshow("salted",g2)
	cv2.imshow("filtered", img_median)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	
