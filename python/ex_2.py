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



# Function that give you the ability to rotate any image with a specific angle
def rotate(image = "onion.png", angle = 45, center = None, scale = 1.0):

	"""
	args: 
		- image: absolute path to the image
		- angle: ex. 45°
	"""
	# read the image
	img = cv.imread(image)
	# retrieve the height and width
	(h, w) = img.shape[:2]
	# Check if the center is precized or not
	if center is None:
		center = (w / 2, h / 2)
	# Perform the rotation
	M = cv.getRotationMatrix2D(center, angle, scale)
	# Apply the rotation matrix to the image
	rotated = cv.warpAffine(img, M, (w, h))
	# Show the images
	cv.imshow("Original Image", img)
	cv.imshow('Rotated Image', rotated)

	# Don't destroy the images until the user do
	cv.waitKey()
	cv.destroyAllWindows()

# Rotate with default params
rotate()
# Rotate with 90°
rotate(angle = 90)
#Rotate with -45°
rotate("onion.png", -45)


