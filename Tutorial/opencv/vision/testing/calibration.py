        #image processing differentiate btw red and ble
        #input to arduino
        #area of contour
import cv2
import numpy as np
import serial
import time
import requests


def nothing(int):
            #any operation
    pass
roiframe=cv2.VideoCapture('vision1.mp4')



            #   input
#url="http://172.17.56.185:8080/shot.jpg"
        #calibration
        # Create a window
cv2.namedWindow('red')
        # create trackbars for color change
cv2.createTrackbar('lowH','red',0,179,nothing)
cv2.createTrackbar('highH','red',179,179,nothing)
         
cv2.createTrackbar('lowS','red',0,255,nothing)
cv2.createTrackbar('highS','red',255,255,nothing)
         
cv2.createTrackbar('lowV','red',0,255,nothing)
cv2.createTrackbar('highV','red',255,255,nothing)

        # Create a window
cv2.namedWindow('blue')
        # create trackbars for color change
cv2.createTrackbar('lowH','blue',0,179,nothing)
cv2.createTrackbar('highH','blue',179,179,nothing)
         
cv2.createTrackbar('lowS','blue',0,255,nothing)
cv2.createTrackbar('highS','blue',255,255,nothing)
         
cv2.createTrackbar('lowV','blue',0,255,nothing)
cv2.createTrackbar('highV','blue',255,255,nothing)

        # Create a window
cv2.namedWindow('green')
        # create trackbars for color change
cv2.createTrackbar('lowH','green',0,179,nothing)
cv2.createTrackbar('highH','green',179,179,nothing)
         
cv2.createTrackbar('lowS','green',0,255,nothing)
cv2.createTrackbar('highS','green',255,255,nothing)
         
cv2.createTrackbar('lowV','green',0,255,nothing)
cv2.createTrackbar('highV','green',255,255,nothing)



while True:
           # img_resp=requests.get(url)
           # img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
           # frame=cv2.imdecode(img_arr,-1)
            _,frame=roiframe.read()
            rows,cols,channels=frame.shape
            frame=frame[int(rows/4):,:]
            cv2.imshow('frame',frame)
            rows=int(rows/4)
            rows,cols,channels=frame.shape
            #calibrations
            # get current positions of the trackbars
            red_ilowH = cv2.getTrackbarPos('lowH', 'red')
            #red_ilowH=110
            red_ihighH = cv2.getTrackbarPos('highH', 'red')
            #red_ihighH=130
            red_ilowS = cv2.getTrackbarPos('lowS', 'red')
            #red_ilowS=50
            red_ihighS = cv2.getTrackbarPos('highS', 'red')
            #red_ihighS=255
            red_ilowV = cv2.getTrackbarPos('lowV', 'red')
            #red_ilowV=50
            red_ihighV = cv2.getTrackbarPos('highV', 'red')
            #red_ihighH=255
            # get current positions of the trackbars
            blue_ilowH = cv2.getTrackbarPos('lowH', 'blue')
            #blue_ilowH=78
            blue_ihighH = cv2.getTrackbarPos('highH', 'blue')
            #blue_ihighH=138
            blue_ilowS = cv2.getTrackbarPos('lowS', 'blue')
            #blue_ilowS=158
            blue_ihighS = cv2.getTrackbarPos('highS', 'blue')
            #blue_ihighH=255
            blue_ilowV = cv2.getTrackbarPos('lowV', 'blue')
            #blue_ilowV=124
            blue_ihighV = cv2.getTrackbarPos('highV', 'image')
            #blue_ihighV=255
            # get current positions of the trackbars
            green_ilowH = cv2.getTrackbarPos('lowH', 'green')
            #green_ilowH=60
            green_ihighH = cv2.getTrackbarPos('highH', 'green')
            #green_ihighH=75
            green_ilowS = cv2.getTrackbarPos('lowS', 'green')
            #green_ilowS=100
            green_ihighS = cv2.getTrackbarPos('highS', 'green')
            #green_ihighS=255
            green_ilowV = cv2.getTrackbarPos('lowV', 'green')
            #green_ilowV=50
            green_ihighV = cv2.getTrackbarPos('highV', 'green')
            #green_ihighV=255

            #write default vaue range of red,green and blue
            # get current positions of the trackbars
            upper_red_hsv=np.array([red_ihighH, red_ihighS, red_ihighV])
            lower_red_hsv= np.array([red_ilowH, red_ilowS, red_ilowV])
            upper_blue_hsv= np.array([blue_ihighH, blue_ihighS, blue_ihighV])
            lower_blue_hsv=np.array([blue_ilowH, blue_ilowS, blue_ilowV])
            upper_green_hsv=np.array([green_ihighH, green_ihighS, green_ihighV])
            lower_green_hsv=np.array([green_ilowH, green_ilowS, green_ilowV])
            
            #open cv processing
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            image=cv2.threshold(frame,100,255,cv2.THRESH_BINARY)

            #morphological transformation
            mask_red=cv2.inRange(hsv,lower_red_hsv,upper_red_hsv)
            kernel=np.ones((5,5),np.uint8)
            mask_red=cv2.erode(mask_red,kernel)
            
            mask_blue=cv2.inRange(hsv,lower_blue_hsv,upper_blue_hsv)
            kernel=np.ones((5,5),np.uint8)
            mask_blue=cv2.erode(mask_blue,kernel)
            
            
            mask_green=cv2.inRange(hsv,lower_green_hsv,upper_green_hsv)
            kernel=np.ones((5,5),np.uint8)
            mask_green=cv2.erode(mask_green,kernel)
            
            

            #adaptive threshold can be used to make mask more clear
            
            result_red=cv2.bitwise_and(frame,frame,mask=mask_red)
            result_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
            result_green=cv2.bitwise_and(frame,frame,mask=mask_green)
            #cv2.imshow('re_blue',result_blue)
            #cv2.imshow('re_red',result_red)
            cv2.imshow('re_green',result_green)
            #cv2.imshow('frame',frame)
            
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
               break
            
roiframe.release()
cv2.destroyAllWindows()
