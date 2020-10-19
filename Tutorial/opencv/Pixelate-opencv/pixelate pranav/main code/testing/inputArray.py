import numpy as np
import cv2
#input
'''
input image or video
'''
input_bgr=cv2.imread('tacarena.jpg')
#settng up processing values
rows_input,cols_input=input_bgr.shape[:2]
input_hsv=cv2.cvtColor(input_bgr,cv2.COLOR_BGR2HSV)
'''
change here 5 to 9
'''
flag_x=int(rows_input/5)
flag_y=int(cols_input/5)
'''
white shape=0
red circle=1
red square=2
yellow cirle=3
yellow square=4
blue square=5
'''
'''
calibrate the values
'''
#output array
'''
change here 5 to 9
'''
output=np.zeros((5,5),np.uint8)
#values
lower_red=np.array([0,40,0])
upper_red=np.array([14,255,255])
lower_yellow=np.array([7,40,0])
upper_yellow=np.array([50,255,255])
lower_blue=np.array([95,40,0])
upper_blue=np.array([110,255,255])

#mask
mask_red=cv2.inRange(input_hsv,lower_red,upper_red)
mask_yellow=cv2.inRange(input_hsv,lower_yellow,upper_yellow)
mask_blue=cv2.inRange(input_hsv,lower_blue,upper_blue)

#morph
'''
check here for kernel
'''
kernel=np.ones((5,5),dtype=np.uint8)
mask_red=cv2.morphologyEx(mask_red,cv2.MORPH_OPEN,kernel)
mask_yellow=cv2.morphologyEx(mask_yellow,cv2.MORPH_OPEN,kernel)
mask_blue=cv2.morphologyEx(mask_blue,cv2.MORPH_OPEN,kernel)
mask_red=cv2.dilate(mask_red,kernel)
mask_yellow=cv2.dilate(mask_yellow,kernel)
mask_blue=cv2.dilate(mask_blue,kernel)
cv2.imshow('mask_red',mask_red)
##cv2.imshow('mask_yellow',mask_yellow)
##cv2.imshow('mask_blue',mask_blue)

#contours
cnt_red,_=cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt_yellow,_=cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt_blue,_=cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#approx,moments for red
for cnt in cnt_red:
    area=cv2.contourArea(cnt)
    if area>50:
        approx_red=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
        cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
        M=cv2.moments(approx_red)
        if(M["m00"]!=0):
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
            #calculating position of shape in output array
            col_red=int(cX/flag_x)
            row_red=int(cY/flag_y)
            if(len(approx_red)==4):
                output[row_red][col_red]=2
            if(len(approx_red)>4):
                output[row_red][col_red]=1
#approx,moments for yellow

for cnt in cnt_yellow:
    area=cv2.contourArea(cnt)
    if area>50:
        approx_yellow=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
        cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
        M=cv2.moments(approx_yellow)
        if(M["m00"]!=0):
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
            #calculating position of shape in output array
            col_yellow=int(cX/flag_x)
            row_yellow=int(cY/flag_y)
            if(len(approx_yellow)==4):
                output[row_yellow][col_yellow]=4
            if(len(approx_yellow)>4):
                output[row_yellow][col_yellow]=3

#approx moments for blue
for cnt in cnt_blue:
    area=cv2.contourArea(cnt)
    if area>50:
        approx_blue=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
        cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
        M=cv2.moments(approx_blue)
        if(M["m00"]!=0):
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
            #calculating position of shape in output array
            col_blue=int(cX/flag_x)
            row_blue=int(cY/flag_y)
            if(len(approx_blue)==4):
                output[row_blue][col_blue]=5
            
cv2.imshow('output',input_bgr)
print(output)
