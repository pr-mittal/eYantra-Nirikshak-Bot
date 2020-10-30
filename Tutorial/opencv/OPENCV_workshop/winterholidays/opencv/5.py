import numpy as np
import cv2

img1=cv2.imread('matplotlib1.jpg')
img2=cv2.imread('matplotlib2.jpg')
'''
>>> x = np.uint8([250])
>>> y = np.uint8([10])
>>> print( cv.add(x,y) ) # 250+10 = 260 => 255
[[255]]
>>> print( x+y )          # 250+10 = 260 % 256 = 4
[4]
'''
#add =img1 +img2;
#add=cv2.add(img1,img2)
#cv2.imshow('add',add)
'''
This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. Images are added as per the equation below:

g(x)=(1−α)f0(x)+αf1(x)
By varying α from 0→1, you can perform a cool transition between one image to another.

Here I took two images to blend them together. First image is given a weight of 0.7 and second image is given 0.3. cv.addWeighted() applies following equation on the image.

dst=α⋅img1+β⋅img2+γ
'''
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

