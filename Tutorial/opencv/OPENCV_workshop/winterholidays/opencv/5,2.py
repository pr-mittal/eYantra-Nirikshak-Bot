import cv2
import numpy as np

img1 = cv2.imread('matplotlib2.jpg')
img2=cv2.imread('python.png')
rows,cols,channels=img2.shape

roi=img1[0:rows,0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

'''
Python: cv2.bitwise_and(src1, src2[, dst[, mask]]) → dst
Python: cv.And(src1, src2, dst, mask=None) → None
Python: cv.AndS(src, value, dst, mask=None) → None
Parameters:	
src1 – first input array or a scalar.
src2 – second input array or a scalar.
src – single input array.
value – scalar value.
dst – output array that has the same size and type as the input arrays.
mask – optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed.
mask basically tells the region where bitwise and operation is to be performed in src1 and src2
'''
'''
by seeing mask we saw that the symbol region is black and other region nearby is white.
so we do the dot product of it with the img1 to create a black empty space for the symbol in img1
as for white region 1*a=a the region except where the symbol has to coe is unaffected
and using mask_inv with img2 we get only the colored symbol part
then we add both of them to get mixed image
'''
img1_bg=cv2.bitwise_and(roi,roi,mask=mask)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst
#print(ret),its value is 220
cv2.imshow('res',img1)
#cv2.imshow('img1',img1)
#cv2.imshow('mask',mask)
#cv2.imshow('img1_bg',img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
