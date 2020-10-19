"""
Opencv Workshop File
Can be downloaded from bit.ly/35yQrxW

Open This file in IDLE and uncomment the relevant parts by selecting and pressing Alt+4
Use Alt+3 to comment selected line.
"""

import numpy as np
import cv2

# Read Images......................................................READ HERE: https://bit.ly/308E9uP

butterfly = cv2.imread("butterfly.jpg")
baloon = cv2.imread('balloons.jpg')
sydney = cv2.imread("sydney.jpg",0 )
bigk = cv2.imread('bigk.jpg',0)
smallk = cv2.imread('smallk.jpg',0)

##print(butterfly.shape)
##print(baloon.shape)
##cv2.imshow('fly',butterfly)
##cv2.imshow('bal',baloon)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# Resized and Arithmetic............................................................................

##new_butterfly = cv2.resize(butterfly,(baloon.shape[1],baloon.shape[0]))
##new_baloon = baloon/2
##cv2.imshow('dull',new_baloon)
##cv2.imshow('resize',new_butterfly)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# Writing and Cropping.............................................................................

##crop_butterfly = butterfly[200:250,100:156,:]
##cv2.imwrite('cut_butterfly.jpeg',crop_butterfly)
##cv2.imshow('cut',crop_butterfly)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# Colorspaces......................................................................................

##for i in range(3):
##    layer=butterfly[:,:,i]  
##    cv2.imshow(str(i),layer)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

##gray = cv2.cvtColor(butterfly,cv2.COLOR_BGR2GRAY)
##hsv = cv2.cvtColor(butterfly, cv2.COLOR_BGR2HSV)
##lab = cv2.cvtColor(butterfly, cv2.COLOR_BGR2LAB)
##
##cv2.imshow('gray',gray)
##cv2.imshow('hsv',hsv)
##cv2.imshow('lab',lab)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# Thresholding......................................................READ HERE: https://bit.ly/307gmeS

##lower_green = np.array([0,50,0])
##upper_green = np.array([100,255,100])
##green =cv2.inRange(butterfly,lower_green,upper_green)
##cv2.imshow('green',green)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# Morpho...........................................................READ HERE:  https://bit.ly/2uC9RoO

##kernel = np.ones((4,4),np.uint8)
##cleank = cv2.erode(bigk,kernel,iterations = 10)
##goodk = cv2.dilate(smallk,kernel,iterations = 5)
##cv2.imshow('cleank',cleank)
##cv2.imshow('goodk',goodk)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# Video............................................................................................

##cap = cv2.VideoCapture(0) ##('begin.mkv')
##while True:
##    ret,img = cap.read()
##    if ret == False:
##        break
##    # Processing Here
##    cv2.imshow('vid',img)
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##cap.release()
##cv2.destroyAllWindows()

