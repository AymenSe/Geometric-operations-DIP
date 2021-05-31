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


# Load image
I = cv.imread("rose.jpeg")

# Extract height and width and channels
j, k, c = I.shape

# Scale factor
scale = 17

# Contruct new height and width based on new scale factor
x_new = round(j/scale)
y_new = round(k/scale)

print(x_new, y_new)
# Initialized a black image with the new scaled height and width
M = np.zeros((x_new, y_new, c), dtype="uint8")

# build the new scaled image
for ch in range(c): # loop through the channels
	for count1 in range(x_new): # loop through the new cols
		for count2 in range(y_new): # loop through the lines
			M[count1, count2, ch] = I[count1*scale, count2*scale, ch] # assigning to every pixel of the black image a new value


# plot the original image and the sampled image
cv.imshow("I Image", I)
cv.imshow('M Image', M)


cv.waitKey()
cv.destroyAllWindows()