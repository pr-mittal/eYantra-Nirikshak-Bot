import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
        _,frame=cap.read()
        #hsv means hue(type of color),saturation(how visible is the color),value or brightness, READ word file
        hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_red=np.array([90,150,0])
        upper_red=np.array([255,255,255])
        '''
dark_red  = np.uint8([[[12,22,121]]])
    dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
The result here will be an HSV value that is identical to the dark_red value. This is great... but again... you run into the fundamental problem with ranges in colors vs ranges in HSV. They are just fundamentally different. You may have a legitimate use for BGR ranges, they will still work, but for detecting one "color," it wont work well.

        '''
        #inrange-if the values of the hsv are between lower boundary and upper boundary then it gets value 0 or otherwise 1 , basically used for threshholding images
        mask=cv2.inRange(hsv,lower_red,upper_red)
        
        res=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)
        cv2.imshow('res',res)
        k=cv2.waitKey(5) & 0xff
        if k==27:
            break
cap.release()
cv2.destroyAllWindows()
