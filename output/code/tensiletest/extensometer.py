import matplotlib.pyplot as plt
import matplotlib.image as mping
from PIL import Image
import numpy as np
#%matplotlib inline
import sys
import numpy as np

import cv2

print(cv2.__version__)

img = cv2.imread('red_dots.jpg',1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
low = np.array([0,0,0])
high = np.array([255,0,0])
red_mask = cv2.inRange(img, low, high)
res1 = cv2.bitwise_and(img,img, mask=red_mask)
cv2.imshow('res',res1)
cv2.waitKey(0)



hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv image',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(hsv, cmap = 'hsv', interpolation = 'bicubic')
plt.show()

lower_red = np.array([170,80,118])
upper_red= np.array([176,180,150])
mask = cv2.inRange(hsv, lower_red, upper_red)


res = cv2.bitwise_and(hsv,hsv, mask= mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#import skimage
#from skimage import data

#print(sys.)
#img = Image.open('red_dots.JPG')
#img = mping.imread('red_dots.JPG')
#img_plot = plt.imshow(img)
#plt.show()

#hsv = color.rgb2hsv(img)
#%matplotlib qt
#plt.imshow(hsv)
#plt.show()