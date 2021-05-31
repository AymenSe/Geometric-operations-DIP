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

# Resized image based on Nearest method interpolation
resized_img = cv.resize(onion_img, (512, 512), interpolation = cv.INTER_NEAREST)

cv.imshow("Original Image", onion_img)
cv.imshow('Resized Image', resized_img)
cv.waitKey()
cv.destroyAllWindows()