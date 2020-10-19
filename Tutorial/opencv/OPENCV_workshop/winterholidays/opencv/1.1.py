import cv2
import numpy as np
import matplotlib.pyplot as plt

#                                   0
img= cv2.imread('opencv1.jpeg',cv2.IMREAD_GRAYSCALE)
#EACH type of colour has a number like grayscale has 0
#IMREAD__COLOR = 1
#IMREAD__UNCHANGED = -1

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
