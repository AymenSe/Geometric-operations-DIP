####################################################  
#
# 	@ Authors : SEKHRI Aymen
# 				MOHAMMED HACENE Tarek
#	
# 	@ Hint: you have to install all requirements
# 			from requirements.txt                    
#
####################################################  

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# load the image
onion_img = cv.imread("onion.png")

# Store height and width and channels of the image
row, col, chs = onion_img.shape

# Store the spectral resolution
dtype_img = onion_img.dtype # This will give you: uint8

def translation(img, trans):

	"""
	args: 
		- img: absolute path to the image
		- trans: must be a tuple (row_trans, col_trans)
	"""
	# read the image
	image = cv.imread(img)
	# retrieve the height and the width
	height, width = image.shape[:2]
	# retrieve the params of translation
	row_trans, col_trans = trans
	# Create the translation matrix
	T = np.float32([[1, 0, col_trans], [0, 1, row_trans]])
	# Apply the T matrix: T*M 
	img_translation = cv.warpAffine(image, T, (width, height))
	# show the images
	cv.imshow("Original Image", image)
	cv.imshow('Translation Image', img_translation)

	# Don't destroy the images until the user do
	cv.waitKey()
	cv.destroyAllWindows()


# translation 20 pixel to the right
translation("onion.png", (0, 20))
# translation 50 lines and 100 cols to the right
translation("onion.png", (50, 100))
# remove the peper from the image using translations
translation("onion.png", (40, 40))



