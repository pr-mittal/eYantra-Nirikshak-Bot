import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel=np.ones((5,5),np.uint8)
    #takes 5 by 5 pixel area and if there are any black pixels then all the region is done black
    erosion=cv2.erode(mask,kernel,iterations=1)
    #in (5,5) does the whole region white if one of them is white
    dilation=cv2.dilate(mask,kernel,iterations=1)
    #iteration is number of times erode or dilate is done
    #removes the noise
    #opening removes false positives i.e white pixels alone in the mask here and there
    #closing removes false negatives i.e. black pixels alone here and there
    opening =cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing =cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    tophat =cv2.morphologyEx(mask,cv2.MORPH_TOPHAT ,kernel)
    blackhat =cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)
    

    # It is the difference between input image and Opening of the image
    cv2.imshow('Tophat',tophat)

    # It is the difference between the closing of the input image and input image.
    cv2.imshow('Blackhat',blackhat)

    
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation',dilation)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
