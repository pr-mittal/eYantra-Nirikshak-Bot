import numpy as np
import cv2

img =cv2.imread('matplotlib2.jpg',cv2.IMREAD_COLOR)
img[55,55]=[255,255,255]
px=img[55,55]
print(px)

#region  of image(roi)
roi=img[550:600,550:600]
img[100:150,100:150]=[255,255,255]
img[0:50,0:50]=roi;
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
