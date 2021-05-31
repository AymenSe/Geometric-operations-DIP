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
rose_img = cv.imread("rose.jpeg")

# Extract the (r --> height) and (c --> width) and ( w --> channels )
r, c, w = rose_img.shape

# Maximum pissble number of intensity values used in the quantization of the orginal image
B = 256

# the desired maximum pissble number of intensity values used in the quantization of the new image
#q = 4
#q = 8
#q = 14
q = int(input("Enter the number of quantization values: "))

# l divides the B intrval [0-255] into multiple ranges each range has length of l
l = B/q

# Array of zeros
E = np.zeros((256,1))

# Generate the quantization function
for i in range(256):
	E[i,0] = (i // l) * l + l/2

# plot the quantization function
plt.plot(np.arange(0, 256, 1), E)
plt.show()


# Generate a black image with the same size of the original image
y = np.zeros(rose_img.shape, dtype="uint8") # change dtype from double to uint8 for better visualisation

# Generate the new image with the new intensity values
for ch in range(w):
	for i in range(r):
		for j in range(c):
			y[i, j, ch] = E[rose_img[i, j, ch], 0]


# plot the new image
cv.imshow('y Image', y)

cv.waitKey()
cv.destroyAllWindows()