#settng up processing values
import cv2
import numpy as np
frame=cv2.imread('tac.jpg')
input_bgr=frame
input_gray=cv2.cvtColor(input_bgr,cv2.COLOR_BGR2GRAY)
rows_input,cols_input=input_bgr.shape[:2]
print(rows_input)
print(cols_input)
input_hsv=cv2.cvtColor(input_bgr,cv2.COLOR_BGR2HSV)

'''
change here 5 to 9
'''
flag_x=int(cols_input/5)
print(flag_x)
flag_y=int(rows_input/5)
print(flag_y)
'''
white shape=0
red circle=1
red square=2
yellow cirle=3
yellow square=4
blue square=5
green square=6
'''
'''
calibrate the values
'''
#output array
'''
change here 5 to 9
'''
output=np.zeros((5,5),np.uint8)
green_matrix=np.zeros((5,5),np.uint8)
#values
lower_red=np.array([0,45,59])
upper_red=np.array([24,255,255])
lower_yellow=np.array([20,90,69])
upper_yellow=np.array([68,255,255])
lower_green=np.array([41,32,58])
upper_green=np.array([87,255,255])
lower_white=np.array([0,0,191])
upper_white=np.array([179,87,255])

#mask
mask_red=cv2.inRange(input_hsv,lower_red,upper_red)
mask_yellow=cv2.inRange(input_hsv,lower_yellow,upper_yellow)
mask_green=cv2.inRange(input_hsv,lower_green,upper_green)
#_,mask_white=cv2.threshold(input_gray,220,255,cv2.THRESH_BINARY)
mask_white=cv2.inRange(input_hsv,lower_white,upper_white)
#morph
'''
check here for kernel
'''
kernel=np.ones((5,5),dtype=np.uint8)
mask_red=cv2.morphologyEx(mask_red,cv2.MORPH_OPEN,kernel)
mask_yellow=cv2.morphologyEx(mask_yellow,cv2.MORPH_OPEN,kernel)
mask_green=cv2.morphologyEx(mask_green,cv2.MORPH_OPEN,kernel)
mask_white=cv2.morphologyEx(mask_white,cv2.MORPH_OPEN,kernel)
mask_red=cv2.dilate(mask_red,kernel)
mask_yellow=cv2.dilate(mask_yellow,kernel)
mask_green=cv2.dilate(mask_green,kernel)
mask_white=cv2.dilate(mask_white,kernel)
cv2.imshow('mask_red',mask_red)
cv2.imshow('mask_yellow',mask_yellow)
cv2.imshow('mask_white',mask_white)
cv2.imshow('mask_green',mask_green)

#contours
cnt_red,_=cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt_yellow,_=cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt_green,_=cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt_white,_=cv2.findContours(mask_white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#approx,moments for red
for cnt in cnt_red:
    area=cv2.contourArea(cnt)
    if area>50:
        '''
check value of 0.05
'''
        approx_red=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
        cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
        M=cv2.moments(approx_red)
        if(M["m00"]!=0):
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
            #calculating position of shape in output array
            col_red=int(cX/flag_x)
            print(col_red)
            row_red=int(cY/flag_y)
            print(row_red)
            if(len(approx_red)==4):
                output[row_red][col_red]=2
            if(len(approx_red)>4):
                output[row_red][col_red]=1

#approx,moments for yellow

for cnt in cnt_yellow:
    area=cv2.contourArea(cnt)
    if area>50:
        '''
check value of 0.05
'''
        approx_yellow=cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
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

#approx moments for green
for cnt in cnt_green:
    area=cv2.contourArea(cnt)
    if area>50:
        approx_blue=cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
        cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
        M=cv2.moments(approx_blue)
        if(M["m00"]!=0):
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
            #calculating position of shape in output array
            col_blue=int(cX/flag_x)
            row_blue=int(cY/flag_y)
            if(len(approx_blue)==4):
                green_matrix[row_blue][col_blue]=6
#position of blue is fixed
'''output[8][5]=5
output[8][4]=5
output[8][6]=5
output[5][5]=5'''
#make a mask for white and update values after updating values due to blue mask 
for cnt in cnt_white:
    area=cv2.contourArea(cnt)
    if area>50:
        '''
check value of 0.05
'''
        approx_white=cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
        cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
        M=cv2.moments(approx_white)
        if(M["m00"]!=0):
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
            #calculating position of shape in output array
            col_white=int(cX/flag_x)
            row_white=int(cY/flag_y)
            if(len(approx_white)==4):
                output[row_white][col_white]=0
cv2.imshow('frame',frame)
print(output)
print(green_matrix)
