import numpy as np
import cv2

img=cv2.imread('bookpage.jpg')
'''
Python: cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst
Python: cv.AdaptiveThreshold(src, dst, maxValue, adaptive_method=CV_ADAPTIVE_THRESH_MEAN_C, thresholdType=CV_THRESH_BINARY, blockSize=3, param1=5) → None¶
Parameters:	
src – Source 8-bit single-channel image.
dst – Destination image of the same size and the same type as src .
maxValue – Non-zero value assigned to the pixels for which the condition is satisfied. See the details below.
adaptiveMethod – Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C . See the details below.
thresholdType – Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV .
blockSize – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.
C – Constant subtracted from the mean or weighted mean (see the details below). Normally, it is positive but may be zero or negative as well.
'''
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
#grayscaled
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#adaptive thresholding
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#otsu threshold
retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


print(retval)#12.0
print(retval2)#22.0
cv2.imshow('bookpage',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()
