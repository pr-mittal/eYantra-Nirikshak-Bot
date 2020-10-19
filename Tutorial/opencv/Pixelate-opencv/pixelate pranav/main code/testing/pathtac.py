#importing liraries
import cv2
import numpy as np
import serial
import time
import cv2.aruco as aruco
cap=cv2.VideoCapture('output.avi')
ser=serial.Serial('COM5',9600)
'''
0 9  18 27 36 45 54 63 72
1 10 19
2 11 20
3 12 21
4 13
5 14
6 15
7 16
8 17 26 35 44 53 62 71 80
'''
'''
calibrate time
'''
# part ofdjikstars algorithm
#add here
def djikstras(current_pos,fianl_pos,input_array,extension=0,min_color=7):
    d_arr=np.full((5,5),np.inf)
    v_arr=np.full((5,5),np.inf)
    p_arr=np.full((5,5),np.inf)

    arr=input_array

    for n in range(len(arr)):
        arr[n]=[0]+arr[n]+[0]
    arr=[[0,0,0,0,0,0,0]]+arr+[[0,0,0,0,0,0,0]]
    
    '''arr=np.array([[0,0,0,0,0,0,0,0,0,0,0],
                  [0,1,2,3,4,3,4,1,3,1,0],
                  [0,1,4,2,2,1,4,3,1,1,0],
                  [0,2,3,1,4,2,1,1,3,2,0],
                  [0,4,1,4,1,0,3,4,1,2,0],
                  [0,1,4,3,0,0,0,2,1,4,0],
                  [0,4,3,4,2,0,1,1,2,3,0],
                  [0,1,1,4,3,1,3,4,2,1,0],
                  [0,4,2,3,1,1,3,1,2,4,0],
                  [0,2,2,1,4,3,3,1,4,2,0],
                  [0,0,0,0,0,0,0,0,0,0,0]])'''

    def dspa(a,b,c,d,e):
        if arr[a+1][b+1]!=0:
            if d_arr[a][b]>c:
                if arr[a+1][b+1]!=min_color:
                    d_arr[a][b]=c+1
                    p_arr[a][b]=d
                    v_arr[a][b]=e+1
                elif arr[a+1][b+1]==min_color:
                    d_arr[a][b]=c
                    p_arr[a][b]=d
                    v_arr[a][b]=e+1
        return arr

    si=current_pos[0]+1
    sj=current_pos[1]+1
    di=final_pos[0]+1
    dj=final_pos[1]+1

    d_arr[si-1][sj-1]=0
    p_arr[si-1][sj-1]=0
    v_arr[si-1][sj-1]=0

    arr1=[[si-1,sj-1]]
    e=0

    def start(si,sj):
        dspa(si+1,sj,d_arr[si][sj],10*(si+1)+sj+1,e)
        dspa(si,sj+1,d_arr[si][sj],10*(si+1)+sj+1,e)
        dspa(si-1,sj,d_arr[si][sj],10*(si+1)+sj+1,e)
        dspa(si,sj-1,d_arr[si][sj],10*(si+1)+sj+1,e)

    while len(arr1)!=0:
        for x in arr1:
            if x[0]!=di or x[1]!=dj:
                start(x[0],x[1])
        e+=1
        arr2=np.where(v_arr==e)
        arr1=list(zip(arr2[0],arr2[1]))
        
    path=[di-1+(dj-1)*5]
    p=p_arr[di-1][dj-1]
    p=int(p)
    p2=(int(p/10)-1+(p%10-1)*5)
    while(p!=0):
        path.append(p2)
        p=p_arr[int(p/10)-1][p%10-1]
        p2=(int(p/10)-1+(int(p%10)-1)*5)
        p=int(p)
        
    path.reverse()
    print(path)
    return(path)

def angle_between(v1, v2):
    return np.angle(v2/v1,deg=True)

#make the bot follow the path as directed
def pathFolllower(frame,path,current_pos,roi=[0,0,np.inf,np.inf]):
    #align the bot
    row,col=frame.shape[:2]
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    threshold=np.inf
    #make the bot follow the path
    for i in range(1,len(path)-1):
        while True:
             _,frame=cap.read()
             frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
             cent,current_pos,v1=aruco_marker(frame_gray,roi)
             v2=[((path[i]%9-1)*col/9+((path[i]%9)*col/9))/2-cent[0],((path[i]/9-1)*row/9+((path[i]/9)*row/9)/2-cent[1])]
             v2=complex(v2[0],v2[1])
             centroid=[((path[i]%9-1)*col/9+((path[i]%9)*col/9))/2,((path[i]/9-1)*row/9+((path[i]/9)*row/9))/2]
             m=cv2.Moments(centroid-cent)
             threshold=sqrt(m["m20"]+m["m02"])
             angle=anglebetween(v1,v2)
             if(angle>30):
                 ser.write(b'L')
                 '''
                 see value
                 '''
                 time.sleep(angle*0.01)
                 ser.write(b'S')
                 
                 
             elif(angle<-30):
                 ser.write(b'R')
                 time.sleep(angle*0.01)
                 ser.write(b'S')
             else:
                ser.write(b'F')
                time.sleep(threshold*0.1)
                ser.write(b'S')
                if(threshold<3):
                    break                 
        '''if(path[i]==(current_pos[0]+current_pos[1]*9)):
            ser.write(b'L')
            time.sleep(2)
            ser.write(b'S')
            ser.write(b'F')
            time.sleep(2)
            ser.write(b'S')
            
        elif(path[i]==(current_pos[0]+current_pos[1]*9)):
            ser.write(b'F')
            time.sleep(2)
            ser.write(b'S')
        elif(path[i]==(current_pos[0]+current_pos[1]*9)):
            ser.write(b'R')
            time.sleep(2)
            ser.write(b'S')
            ser.write(b'F')
            time.sleep(2)
            ser.write(b'S')
    '''
        
    
def input_array(frame,roi,thresh):
    #settng up processing values
    input_bgr=frame
    input_gray=cv2.cvtColor(input_bgr,cv2.COLOR_BGR2GRAY)
    rows_input,cols_input=input_bgr.shape[:2]

    #frame[:,:,0]
    
    
    '''
    change here 5 to 9
    '''
    flag_x=int(cols_input/5)
    flag_y=int(rows_input/5)
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
    '''
    changed here
    '''
    white_min=thresh[0][0]
    white_max=thresh[1][0]
    blue_min=thresh[0][1]
    blue_max=thresh[1][1]
    green_min=thresh[0][2]
    green_max=thresh[1][2]
    yellow_min=thresh[0][3]
    yellow_max=thresh[1][3]
    red_min=thresh[0][4]
    red_max=thresh[1][4]
    output=np.zeros((5,5),np.uint8)
    green_matrix=np.zeros((5,5),np.uint8)
    #values
    lower_red=np.array([max(0,red_min[0]-30),max(0,red_min[1]-30),max(0,red_min[2]-30)])
    upper_red=np.array([min(255,red_max[0]+30),min(255,red_max[1]+30),min(255,red_max[2]+30)])
    lower_yellow=np.array([max(0,yellow_min[0]-30),max(0,yellow_min[1]-30),max(0,yellow_min[2]-30)])
    upper_yellow=np.array([min(255,yellow_max[0]+30),min(255,yellow_max[1]+30),min(255,yellow_max[2]+30)])
    lower_green=np.array([max(0,green_min[0]-45),max(0,green_min[1]-45),max(0,green_min[2]-45)])
    upper_green=np.array([min(255,green_max[0]+45),min(255,green_max[1]+45),min(255,green_max[2]+45)])
    lower_white=np.array([max(0,white_min[0]-30),max(0,white_min[1]-30),max(0,white_min[2]-30)])
    upper_white=np.array([min(255,white_max[0]+30),min(255,white_max[1]+30),min(255,white_max[2]+30)])


    #mask
    mask_red=cv2.inRange(input_bgr,lower_red,upper_red)
    mask_yellow=cv2.inRange(input_bgr,lower_yellow,upper_yellow)
    mask_green=cv2.inRange(input_bgr,lower_green,upper_green)
    #_,mask_white=cv2.threshold(input_gray,220,255,cv2.THRESH_BINARY)
    mask_white=cv2.inRange(input_bgr,lower_white,upper_white)
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
    #cv2.imshow('mask_red',mask_red)
    #cv2.imshow('mask_yellow',mask_yellow)
    ##cv2.imshow('mask_green',mask_green)

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
                row_red=int(cY/flag_y)
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
    output[0][3]=5
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
    print(output)
    return output,green_matrix

#detection of aruco marker
def aruco_marker(frame,roi):
    #arucomarker
    '''
    changed here
    '''
    while True:
        _,frame=cap.read()
        frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        rows,cols=frame.shape[:2]
        aruco_dict=aruco.Dictionary_get(aruco.DICT_5X5_250)
        parameters=aruco.DetectorParameters_create()
        corners,markerIds,_=aruco.detectMarkers(frame_gray,aruco_dict,parameters=parameters)
        if(len(corners)!=0):
            
            '''
            change 5 to 9
            '''
            
            
            v1=complex(((corners[0][0][0]+corners[0][0][1])/2-(corners[0][0][2]+corners[0][0][3])/2)[0],((corners[0][0][0]+corners[0][0][1])/2-(corners[0][0][2]+corners[0][0][3])/2)[1])
            cent=(corners[0][0][0]+corners[0][0][1]+corners[0][0][2]+corners[0][0][3])//4
            current_pos=[int(cent[1]/int(rows/5)),int(cent[0]/int(cols/5))]
            print(corners)
            return cent,current_pos,v1

            


#main program starts
flag_leave=0
flag=0
#selecting region of arena only
_,frame=cap.read()
roi=cv2.selectROI('frame',frame)
frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
#calculating number of white boxes on green in the starting

'''
changed here
'''
while True:
    array,green_matrix=input_array(frame,roi)
    print(green_matrix)
    count_green=np.where(green_matrix==6)
    count_green=list(zip(count_green[0],count_green[1]))
    if(len(count_green)==4):
        break
white_box=np.where(array==0)
white_box=list(zip(white_box[0],white_box[1]))
count_horuxes=0
for x in white_box:
    if(x==count_green[0]) or (x==count_green[1]) or (x==count_green[2])or (x==count_green[3]):
        count_horuxes+=1

while (count_horuxes!=0):
    _,frame=cap.read()
    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
    array,green_matrix=input_array(frame,roi)
    count_horuxes=0
    white_box=np.where(array==0)
    white_box=list(zip(white_box[0],white_box[1]))

    for x in white_box:
        if(x==count_green[0]) or (x==count_green[1]) or (x==count_green[2])or (x==count_green[3]):
            count_horuxes+=1

    _,current_pos,_=aruco_marker(frame,roi)
    white_box=np.where(array==0)[0]
    white_box=list(zip(white_box[0],white_box[1]))
    for x in white_box:
        if(x==count_green[0]) or (x==count_green[1]) or (x==count_green[2])or (x==count_green[3]):
            break
    path=djikstras(current_pos,x,colour_matrix,extension=0,min_colour=0)
    pathFolllower(frame,path,current_pos,roi)
    ser.write(b'G')
    time.sleep(5)
    _,frame=cap.read()
    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
    blue_destination=np.where(frame==5)[0]
    white_box=list(zip(blue_destination[0],blue_destination[1]))
    path=djikstras(current_pos,blue_destination[0],colour_matrix,extension=0,min_colour=0)
    pathFolllower(frame,path,current_pos,roi)
    ser.write(b'R')
    time.sleep(5)
    ser.write(b'P')
    time.sleep(2)
    time.sleep(b'S')
            
            
    white_box=np.where(array==0)[0]
    count_horuxes=0
    for x in white_box:
        if(x==count_green[0]) or (x==count_green[1]) or (x==count_green[2])or (x==count_green[3]):
            count_horuxes+=1
ser.write(b'O')
cv2.destroyAllWindows()
cap.release()
