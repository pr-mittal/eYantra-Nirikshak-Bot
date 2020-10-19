import cv2
import numpy as np
def nothing(int):
    return
cap=cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('lowCanny','image',0,255,nothing)
cv2.createTrackbar('highCanny','image',0,255,nothing)

while True:
    highCanny=cv2.getTrackbarPos('highCanny','image')
    lowCanny=cv2.getTrackbarPos('lowCanny','image')
    
    _,frame=cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    soblex=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobley=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,lowCanny,highCanny)

    
    cv2.imshow('original',frame)
    #cv2.imshow('soblex',soblex)
    #cv2.imshow('sobley',sobley)
    #cv2.imshow('laplacian',laplacian)
    cv2.imshow('edges',edges)


    k=cv2.waitKey(5)& 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
