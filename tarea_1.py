import cv2
import numpy as np
from random import *



img1 = cv2.imread('day.jpg',0)


scale_percent = 35 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
img2 = img
img = img/255


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

#cv2.imwrite(r'C:\Users\SKU 80093\Documents\Python_Scripts\Deep_Learning_ComputerVision\day_salted_test.jpg', g*255)

g2 = g.copy()


def median_filter(data, filter_size):
  #creación de una copia para no trabajar sobre el mismo array procesado.
	data_after = data.copy()
  #Se divide el filtro que el usuario requiere entre 2, el operador floor division lo redondea hacia abajo.
	indice_filtro = filter_size // 2

  # Tomamos de la imagen con ruido sus propiedades de alto y ancho.
	#ancho_img = range(0, int(round(float(data.shape[1])/2,0)))
	ancho_img = range(0,data.shape[1])
	alto_img = range(0,data.shape[0])
	
	
  #Por cada dirección de pixel (alto y ancho) se ejecuta el ciclo de filtrado z y k.
	for pixel_alto in alto_img:
		for pixel_ancho in ancho_img:
      #En este
			temp = []
			for z in range(filter_size):
				if pixel_alto + z - indice_filtro < 0 or pixel_alto + z - indice_filtro > len(data) - 1:
					for c in range(filter_size):
						temp.append(0)
				else:
					for k in range(filter_size):
						if pixel_ancho + z - indice_filtro < 0 or pixel_ancho + indice_filtro > len(data[0]) - 1:
							try:
								temp.append(data[pixel_alto + z - indice_filtro+ randint(-10,10)][pixel_ancho + k - indice_filtro-1])
							except:
								temp.append(0)
						else:
							try:
								temp.append(data[pixel_alto + z - indice_filtro][pixel_ancho + k - indice_filtro+1])
							except:
								temp.append(0)

			temp.sort()
			data_after[pixel_alto][pixel_ancho] = temp[len(temp) // 2]
		#while True:
		#	cv2.imshow("ff", data_after)
		#	if cv2.waitKey(1) & 0xFF == ord('q'):
		#		break

	return data_after

def median_filter2(data, filter_size):
	temp = []
	indexer = filter_size // 2
	window = [
		(i, j)
		for i in range(-indexer, filter_size-indexer)
		for j in range(-indexer, filter_size-indexer)
	]
	index = len(window) // 2
	for i in range(len(data)):
		for j in range(len(data[0])):
			almacen = sorted(0 if (min(i+a, j+b) < 0 or len(data) <= i+a or len(data[0]) <= j+b) else data[i+a][j+b] for a, b in window) [index]
			data[i][j] = sorted(0 if (min(i+a, j+b) < 0 or len(data) <= i+a or len(data[0]) <= j+b) else data[i+a][j+b] for a, b in window) [index]
	return data

def median_filter3(data, filter_size):
	kernel = []
	i_list = []
	j_list = []

	for i in range(-(filter_size // 2), filter_size-(filter_size // 2)):
		for j in range(-(filter_size // 2), filter_size-(filter_size // 2)):
			i_list.append(i)
			j_list.append(j)

	kernel = list(zip(i_list,j_list))
	index = len(kernel) // 2
	
	for alto_foto in range(len(data)):
		for ancho_foto in range(len(data[0])):
			temp = []
			for alto_kernel, ancho_kernel in kernel:
				if (min(alto_foto+alto_kernel, ancho_foto+ancho_kernel) < 0 or len(data) <= alto_foto+alto_kernel or len(data[0]) <= ancho_foto+ancho_kernel):
					temp.append(0)
				else:
					temp.append(data[alto_foto+alto_kernel][ancho_foto+ancho_kernel])
			data[alto_foto,ancho_foto] =sorted(temp)[index]
	return data



#img_median = cv2.medianBlur(g, 3)

img_median2 = median_filter(g2,3)

img_median3 = median_filter3(g2,3)

while True:
	cv2.imshow("original", img)
	cv2.imshow("salted",g2)
#	cv2.imshow("filtered w opencv", img_median)
	cv2.imshow("filtered with algorithm", img_median2)
	cv2.imshow("filtered with algorithm 2", img_median3)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	
