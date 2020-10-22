

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
var=0
            #   input
url="http://172.17.55.153:8080/shot.jpg"
ser=serial.Serial('COM5',9800)
#frame=cv2.VideoCapture(0)


while True:
            img_resp=requests.get(url)
            img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
            frame=cv2.imdecode(img_arr,-1)
            #_,frame=roiframe.read()
            rows,cols,channels=frame.shape
            frame=frame[int(rows/2):,:]
            rows=int(rows/2)
            if(frame.all()==None):
                serial.write(b'S')
                break
            else:
                #calibrations
                # get current positions of the trackbars
                #red_ilowH = cv2.getTrackbarPos('lowH', 'red')
                red_ilowH=150
                #red_ihighH = cv2.getTrackbarPos('highH', 'red')
                red_ihighH=210
                #red_ilowS = cv2.getTrackbarPos('lowS', 'red')
                red_ilowS=50
                #red_ihighS = cv2.getTrackbarPos('highS', 'red')
                red_ihighS=255
                #red_ilowV = cv2.getTrackbarPos('lowV', 'red')
                red_ilowV=50
                #red_ihighV = cv2.getTrackbarPos('highV', 'red')
                red_ihighV=255
                # get current positions of the trackbars
                #blue_ilowH = cv2.getTrackbarPos('lowH', 'blue')
                blue_ilowH=80
                #blue_ihighH = cv2.getTrackbarPos('highH', 'blue')
                blue_ihighH=170
                #blue_ilowS = cv2.getTrackbarPos('lowS', 'blue')
                blue_ilowS=158
                #blue_ihighS = cv2.getTrackbarPos('highS', 'blue')
                blue_ihighS=255
                #blue_ilowV = cv2.getTrackbarPos('lowV', 'blue')
                blue_ilowV=124
                #blue_ihighV = cv2.getTrackbarPos('highV', 'image')
                blue_ihighV=255
                # get current positions of the trackbars
                #green_ilowH = cv2.getTrackbarPos('lowH', 'green')
                green_ilowH=30
                #green_ihighH = cv2.getTrackbarPos('highH', 'green')
                green_ihighH=90
                #green_ilowS = cv2.getTrackbarPos('lowS', 'green')
                green_ilowS=100
                #green_ihighS = cv2.getTrackbarPos('highS', 'green')
                green_ihighS=255
                #green_ilowV = cv2.getTrackbarPos('lowV', 'green')
                green_ilowV=50
                #green_ihighV = cv2.getTrackbarPos('highV', 'green')
                green_ihighV=255

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
                cv2.imshow('mask_red',mask_red)
                
                mask_blue=cv2.inRange(hsv,lower_blue_hsv,upper_blue_hsv)
                mask_blue=cv2.erode(mask_blue,kernel)
                
                
                mask_green=cv2.inRange(hsv,lower_green_hsv,upper_green_hsv)
                mask_green=cv2.erode(mask_green,kernel)
                
                

                #adaptive threshold can be used to make mask more clear
                
                result_red=cv2.bitwise_and(frame,frame,mask=mask_red)
                result_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
                result_green=cv2.bitwise_and(frame,frame,mask=mask_green)

                if 1:    
                
                    contours_red,_= cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    contours_blue,_ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    contours_green,_ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    #cv2.imshow('result_red',result_red)
                    #cv2.imshow('result_blue',result_blue)
                    #cv2.imshow('result_green',result_green)
                    area_red=[]
                    area_blue=[]
                    area_green=[]
                        #when count is less than 3
                    if (var<3):
                            if cv2.countNonZero(mask_red) == 0:
                        
                                print('Rotate\n')
                                ser.write(b'R')
                                time.sleep(0.05)

                            else:
                    
                        
                                for cnt in contours_red:
                                    area_red+=[cv2.contourArea(cnt)]
                                    approx_red=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
                                    cv2.drawContours(frame,[cnt],0,(0,0,0),5)
                                maxcontour_red=area_red[0]
                                maxcontour_index=0
                                for x in range(0,len(contours_red)):
                                    if (int(maxcontour_red)<int(area_red[x])):
                                        maxcontour_index=x
                            #box found
                                if(area_red[x]>=0.7*rows*cols):
                                    print('X\n')
                                    ser.write(b'X')
                                    time.sleep(5)
                                    
                                    var=var+1
                            #send box found
                                # compute the center of the contour

                                M = cv2.moments(contours_red[x])
                                if M["m00"] !=0:
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    if(cX>rows/2+200):
                                    #right
                                        print('R\n')
                                        ser.write(b'R')
                                        time.sleep(0.05)
                                        
                                    elif(cX<rows/2-200):
                                    #left
                                        
                                        print('L\n')
                                        ser.write(b'L')
                                        time.sleep(0.05)
                                        
                                    elif(cX>=rows/2-200) and (cX<=rows/2+200):
                                    #forward
                                        
                                        print('F\n')
                                        ser.write(b'F')
                                        time.sleep(0.05)
                                
                            
                            if cv2.countNonZero(mask_blue) != 0:
                                for cnt in contours_blue:
                                    area_blue +=[ cv2.contourArea(cnt)]
                                    approx_blue=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
                                    cv2.drawContours(frame,[cnt],0,(0,0,0),5)
                                maxcontour_blue=area_blue[0]
                                maxcontour_index=0
                                for x in range(0,len(contours_blue)):
                                    if (int(maxcontour_blue)<int(area_blue[x])):
                                        maxcontour_index=x
                                if(area_blue[x]>0.5*rows*cols):
                                # compute the center of the contour
                                    M_blue = cv2.moments(contours_blue[x])
                                    if M_blue["m00"] !=0:
                                        cX_blue =int( M_blue["m10"] / M_blue["m00"])
                                        cY_blue = int(M_blue["m01"] / M_blue["m00"])
                                    
                                        if(cX_blue>rows/2+200):
                                        #left-right-forward-left-right
                                            '''ser.write(b'L')
                                            time.sleep(1)
                                            ser.write(b'R')
                                            time.sleep(1)
                                            ser.write(b'F')
                                            time.sleep(1)
                                            ser.write(b'L')
                                            time.sleep(1)
                                            ser.write(b'R')
                                            time.sleep(1)'''
                                            
                                            print('V\n')
                                            ser.write(b'V')
                                            time.sleep(0.05)
                                            
                                        elif(cX_blue<rows/2-200):
                                        #right-left-forward-right-left
                                            '''ser.write(b'R')
                                            time.sleep(1)
                                            ser.write(b'L')
                                            time.sleep(1)
                                            ser.write(b'F')
                                            time.sleep(1)
                                            ser.write(b'R')
                                            time.sleep(1)
                                            ser.write(b'L')
                                            time.sleep(1)'''
                                            
                                            print('W\n')
                                            ser.write(b'W')
                                            time.sleep(0.05)
                                            
                                        elif(cX_blue<=rows/2+200)and(cX_blue>=rows/2-200):
                                        #forward
                                            
                                            print('F\n')
                                            ser.write(b'F')
                                            time.sleep(0.05)
                                        


                        #serial reads 3 then start green mode
                            if(var>=3):
                                print('1')
                                #i.e.allblack
                                if cv2.countNonZero(mask_green) == 0:
                                    
                                     
                                    print('Rotategreen\n')
                                    ser.write(b'R')
                                    time.sleep(0.05)
                                     
                                else:
                                    print('3')
                                    for cnt in contours_green:
                                        area_green +=[ cv2.contourArea(cnt)]
                                        approx_green=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
                                        cv2.drawContours(frame,[cnt],0,(0,0,0),5)
                                    maxcontour_green=area_green[0]
                                    maxcontour_index=0
                                    for x in range(0,len(contours_green)):
                                        if (int(maxcontour_green)<int(area_green[x])):
                                            maxcontour_index=x
                            #final destination reached
                                    if(area_green[x]>=0.7*rows*cols):
                                        
                                        print('Z\n')
                                        ser.write(b'Z')
                                        time.sleep(0.05)
                                        break
                            #send final destination variable
                                # compute the center of the contour
                                    M_green = cv2.moments(contours_green[x])
                                    if M_green["m00"]!=0:
                                        cX_green = int(M_green["m10"] / M_green["m00"])
                                        cY_green = int(M_green["m01"] / M_green["m00"])
                                        if(cX_green>rows/2+200):
                                            #right
                                            
                                            print('R\n')
                                            ser.write(b'R')
                                            time.sleep(0.05)
                                            
                                        elif(cX_green<rows/2-200):
                                            #left
                                            
                                            print('L\n')
                                            ser.write(b'L')
                                            time.sleep(0.05)
                                            
                                        elif(cX_green<=rows/2+200)  and (cX_green>=rows/2-200):
                                            #forward
                                            
                                            print('F\n')
                                            ser.write(b'F')
                                            time.sleep(0.05)
                                        
                                    
                                    if cv2.countNonZero(mask_blue) != 0:

                                        for cnt in contours_blue:
                                            area_blue +=[ cv2.contourArea(cnt)]
                                            approx_blue=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
                                            cv2.drawContours(frame,[cnt],0,(0,0,0),5)
                                        maxcontour_blue=area_blue[0]
                                        maxcontour_index=0
                                        for x in range(0,len(contours_blue)):
                                            if (int(maxcontour_blue)<int(area_blue[x])):
                                                maxcontour_index=x
                                        if(area_blue[x]>0.5*rows*cols):
                                    # compute the center of the contour
                                            M_blue = cv2.moments(contours_blue[x])
                                            if M_blue["m00"] !=0:
                                                cX_blue = int(M_blue["m10"] / M_blue["m00"])
                                                cY_blue = int(M_blue["m01"] / M_blue["m00"])
                                        
                                                if(cX_blue>rows/2+200):
                                            #left-right-forward-left-right
                                                '''ser.write(b'L')
                                                time.sleep(1)
                                                ser.write(b'R')
                                                time.sleep(1)
                                                ser.write(b'F')
                                                time.sleep(1)
                                                ser.write(b'L')
                                                time.sleep(1)
                                                ser.write(b'R')
                                                time.sleep(1)'''
                                                    print('V\n')
                                                    ser.write(b'V')
                                                    time.sleep(0.05)
                                                
                                                elif(cX_blue<rows/2-200):
                                        #right-left-forward-right-left
                                                    print('W\n')
                                                    ser.write(b'W')
                                                    time.sleep(0.05)
                                            
                                                elif(cX_blue<=rows/2+200)and(cX_blue>=rows/2-200):
                                        #forward
                                            
                                                    print('F\n')
                                                    ser.write(b'F')
                                                    time.sleep(0.05)

                                    


            if cv2.waitKey(1) & 0xFF == ord('q'):
                ser.write(b'S')
                break






        #end

ser.close()
#frame.release()
cv2.destroyAllWindows()