'''
P greeen
Q blue
O red
'''
#importing liraries
import cv2
import numpy as np
import serial
import time
import math
import cv2.aruco as aruco
cap=cv2.VideoCapture(1)
ser=serial.Serial('COM4',9600)
'''
0 9  18 27 36 45 54 63 72
1 10 19
2 11 20
3 12 21
4 13
5 14
6 15
7 16
8 17 26 35 44 53 62 71 8
calibrate time
'''
# part ofdjikstars algorithm
def djikstras(current_pos,final_pos,input_array,extension=0,min_colour=1):
    print('current_pos=',current_pos)
    print('final_pos',final_pos)
    d_arr=np.full((9,9),np.inf)
    v_arr=np.full((9,9),np.inf)
    p_arr=np.full((9,9),np.inf)

    arr3=input_array
    row,col=arr3.shape
    arr=np.full((11,11),0)
    '''
    chaneged here
    '''
    for x in range(row):
        for y in range(col):
            arr[x+1][y+1]=arr3[x][y]

    '''for n in range(len(arr)):
        np.append(a[n],[0],axis=0)
        np.concatenate((a[n],[0]),axis=0)
    np.append(a,[0,0,0,0,0,0],axis=0)
    
    arr=np.array([[0,0,0,0,0,0,0,0,0,0,0],
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
        if arr[a+1][b+1]!=0 and a!=-1 and b!=-1 and a!=10 and b!=10:
            if d_arr[a][b]>c:
                if arr[a+1][b+1]!=min_colour:
                    d_arr[a][b]=c+1
                    p_arr[a][b]=d
                    v_arr[a][b]=e+1
                elif arr[a+1][b+1]==min_colour:
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
    path=[di-1+(dj-1)*9]
    p=p_arr[di-1][dj-1]
    min_d=np.inf
    '''
    get checked from goyal
    '''
    path+=[0]
    if((di-2)!=-1):
        if(min_d>d_arr[di-2][dj-1]):
            min_d=d_arr[di-2][dj-1]
            p=p_arr[di-2][dj-1]
            path[1]=di-2+(dj-1)*9
    if((dj-2)!=-1):
        if(min_d>d_arr[di-1][dj-2]):
            min_d=d_arr[di-1][dj-2]
            p=p_arr[di-1][dj-2]
            path[1]=di-1+(dj-2)*9
    if((di)!=10):
        if(min_d>d_arr[di][dj-1]):
            min_d=d_arr[di][dj-1]
            p=p_arr[di][dj-1]
            path[1]=di+(dj-1)*9
    if((dj)!=10):
        if(min_d>d_arr[di-1][dj]):
            min_d=d_arr[di-1][dj]
            p=p_arr[di-1][dj]
            path[1]=di-1+(dj)*9
        
    p=int(p)
    p2=(int(p/10)-1+(p%10-1)*9)
    while(p!=0):
        path.append(p2)
        p=p_arr[int(p/10)-1][p%10-1]
        p2=(int(p/10)-1+(int(p%10)-1)*9)
        p=int(p)
        
    path.reverse()
    print('path=',path)
    cv2.waitKey(0)
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
    for i in range(1,len(path)):
        while True:
             print(path[i])
             _,frame=cap.read()
             frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
             cent,current_pos,v1=aruco_marker(frame,roi)
             centroid=[((path[i]//9)*col/9+((path[i]//9 +1)*col/9))/2,((path[i]%9)*row/9+((path[i]%9+1)*row/9))/2]
             v2=[centroid[0]-cent[0],centroid[1]-cent[1]]
             v2=complex(v2[0],v2[1])
             
             a=(centroid-cent)
             threshold=math.sqrt(a[0]*a[0]+a[1]*a[1])
             angle=angle_between(v1,v2)
             print('threshold=',threshold)
             print('angle=',angle)

             if (i==len(path)-1):
                 if (angle<=10)and (angle>=-10):
                     ser.write(b'S')
                     break
                 elif (angle<-10):
                    ser.write(b'L')
                    print('L')
                    '''
                     see value
                    '''
                    time.sleep(abs(angle*0.005))
                    ser.write(b'S')
                 elif (angle>10):
                    ser.write(b'R')
                    print('R')
                    '''
                     see value
                    '''
                    time.sleep(abs(angle*0.005))
                    ser.write(b'S')
                  
             elif(angle<-20):
                 ser.write(b'L')
                 print('L')
                 '''
                 see value
                 '''
                 time.sleep(abs(angle*0.005))
                 ser.write(b'S')
                 
             elif(angle>20):
                 ser.write(b'R')
                 print('R')
                 time.sleep(abs(angle*0.005))
                 ser.write(b'S')
             else:
                if(i!=(len(path)-1)):
                    
                    ser.write(b'F')
                    print('F')
                    
                    time.sleep(abs(threshold*0.01))
                               
                    ser.write(b'S')
             if(threshold<15):
                 print('breaktonext')
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
    cols_input,rows_input=input_bgr.shape[:2]

    #frame[:,:,0]
    
    
    '''
    change here 5 to 9
    '''
    flag_x=int(cols_input/9)
    flag_y=int(rows_input/9)
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
    blue_min=[190,72,40]
    blue_max=[255,190,176]
    
    green_min=thresh[0][2]
    green_max=thresh[1][2]
    yellow_min=thresh[0][3]
    yellow_max=thresh[1][3]
    red_min=thresh[0][4]
    red_max=thresh[1][4]
    output=np.zeros((9,9),np.uint8)
    green_matrix=np.zeros((9,9),np.uint8)
    #values
    lower_red=np.array([max(0,red_min[0]-30),max(0,red_min[1]-30),max(0,red_min[2]-30)])
    upper_red=np.array([min(255,red_max[0]+30),min(255,red_max[1]+30),min(255,red_max[2]+30)])
    lower_yellow=np.array([max(0,yellow_min[0]-30),max(0,yellow_min[1]-30),max(0,yellow_min[2]-20)])
    upper_yellow=np.array([min(255,yellow_max[0]+30),min(255,yellow_max[1]+30),min(255,yellow_max[2]+20)])
    lower_green=np.array([max(0,green_min[0]-20),max(0,green_min[1]-15),max(0,green_min[2]-20)])
    upper_green=np.array([min(255,green_max[0]+20),min(255,green_max[1]+15),min(255,green_max[2]+20)])
    lower_white=np.array([max(0,white_min[0]-20),max(0,white_min[1]-20),max(0,white_min[2]-20)])
    upper_white=np.array([min(255,white_max[0]+15),min(255,white_max[1]+15),min(255,white_max[2]+15)])
    lower_blue=np.array([max(0,blue_min[0]),max(0,blue_min[1]),max(0,blue_min[2])])
    upper_blue=np.array([min(255,blue_max[0]),min(255,blue_max[1]),min(255,blue_max[2])])
    #mask
    mask_red=cv2.inRange(input_bgr,lower_red,upper_red)
    mask_blue=cv2.inRange(input_bgr,lower_blue,upper_blue)
    #mask_blue=cv2.inRange(input_bgr,[8,73,70],[115,200,208])
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
    mask_blue=cv2.morphologyEx(mask_blue,cv2.MORPH_OPEN,kernel)
    mask_yellow=cv2.morphologyEx(mask_yellow,cv2.MORPH_OPEN,kernel)
    mask_green=cv2.morphologyEx(mask_green,cv2.MORPH_OPEN,kernel)
    mask_white=cv2.morphologyEx(mask_white,cv2.MORPH_OPEN,kernel)
    mask_red=cv2.dilate(mask_red,kernel)
    mask_blue=cv2.dilate(mask_blue,kernel)
    mask_yellow=cv2.dilate(mask_yellow,kernel)
    mask_green=cv2.dilate(mask_green,kernel)
    mask_white=cv2.dilate(mask_white,kernel)
    cv2.imshow('mask_red',mask_red)
    cv2.imshow('mask_blue',mask_blue)
    cv2.imshow('mask_yellow',mask_yellow)
    cv2.imshow('mask_green',mask_green)
    cv2.imshow('mask_white',mask_white)
    cv2.waitKey(0)
    #contours
    cnt_red,_=cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt_blue,_=cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
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
            approx_red=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
            cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
            M=cv2.moments(approx_red)
            if(M["m00"]!=0):
                cX=int(M["m10"]/M["m00"])
                cY=int(M["m01"]/M["m00"])
                #calculating position of shape in output array
                col_red=int(cX/flag_x)
                row_red=int(cY/flag_y)
                if(row_red<=8)and(col_red<=8)and (row_red>=0)and (col_red>=0):
                    if(len(approx_red)==4):
                        output[row_red][col_red]=2
                    if(len(approx_red)>4):
                        output[row_red][col_red]=1
#approx,moments for blue
    for cnt in cnt_blue:
        area=cv2.contourArea(cnt)
        if area>50:
            '''
    check value of 0.05
    '''
            approx_blue=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
            M=cv2.moments(approx_blue)
            if(M["m00"]!=0):
                cX=int(M["m10"]/M["m00"])
                cY=int(M["m01"]/M["m00"])
                #calculating position of shape in output array
                col_blue=int(cX/flag_x)
                row_blue=int(cY/flag_y)
                if(row_blue<=8)and(col_blue<=8)and (row_blue>=0)and (col_blue>=0):
                    output[row_blue][col_blue]=5
                    green_matrix[row_blue][col_blue]=5

    #assign value to blue here                
    output[8][3]=5
    output[8][4]=5
    output[8][5]=5
    output[4][4]=5
    green_matrix[4][4]=5
    green_matrix[8][3]=5
    green_matrix[8][4]=5
    green_matrix[8][5]=5
#approx,moments for yellow

    for cnt in cnt_yellow:
        area=cv2.contourArea(cnt)
        if area>50:
            '''
    check value of 0.05
    '''
            approx_yellow=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
            M=cv2.moments(approx_yellow)
            if(M["m00"]!=0):
                cX=int(M["m10"]/M["m00"])
                cY=int(M["m01"]/M["m00"])
                #calculating position of shape in output array
                col_yellow=int(cX/flag_x)
                row_yellow=int(cY/flag_y)
                if(row_yellow<=8)and(col_yellow<=8)and (row_yellow>=0)and (col_yellow>=0):
                    if(len(approx_yellow)==4):
                        output[row_yellow][col_yellow]=4
                    if(len(approx_yellow)>4):
                        output[row_yellow][col_yellow]=3

    #approx moments for green
    for cnt in cnt_green:
        area=cv2.contourArea(cnt)
        if area>50:
            approx_green=cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
            cv2.drawContours(input_bgr,cnt,-1,(0,255,0),3)
            M=cv2.moments(approx_green)
            if(M["m00"]!=0):
                cX=int(M["m10"]/M["m00"])
                cY=int(M["m01"]/M["m00"])
                #calculating position of shape in output array
                col_green=int(cX/flag_x)
                row_green=int(cY/flag_y)
                if(row_green<=8)and(col_green<=8)and (row_green>=0)and (col_green>=0):
                    green_matrix[row_green][col_green]=6
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
                if(row_white<=8)and(col_white<=8)and (row_white>=0)and (col_white>=0):
                    if(len(approx_white)==4):
                        
                        output[row_white][col_white]=0
    #position of blue is fixed
    
    print('output=',output)
    print('green_matrix=',green_matrix)
    return np.array(output),np.array(green_matrix)

#detection of aruco marker
def aruco_marker(frame,roi):
    #arucomarker
    '''
    changed here
    '''
    while True:
        _,frame=cap.read()
        frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rows,cols=frame.shape[:2]
        aruco_dict=aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters=aruco.DetectorParameters_create()
        corners,markerIds,_=aruco.detectMarkers(frame_gray,aruco_dict,parameters=parameters)
        if(len(corners)!=0):
            
            '''
            change 5 to 9
            '''
            
            
            v1=complex(((corners[0][0][0]+corners[0][0][1])/2-(corners[0][0][2]+corners[0][0][3])/2)[0],((corners[0][0][0]+corners[0][0][1])/2-(corners[0][0][2]+corners[0][0][3])/2)[1])
            cent=(corners[0][0][0]+corners[0][0][1]+corners[0][0][2]+corners[0][0][3])//4
            current_pos=[int(cent[1]//int(rows/9)),int(cent[0]//int(cols/9))]
            print('cent=',cent,'current_pos',current_pos)
            return cent,current_pos,v1
        else:
            print("aruco not detected")



#main program starts
flag_leave=0
flag=0
#selecting region of arena only
_,frame=cap.read()
roi=cv2.selectROI('frame',frame)

frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
roi_red=cv2.selectROI('red',frame)
roi_blue=cv2.selectROI('blue',frame)
roi_green=cv2.selectROI('green',frame)
roi_green_2=cv2.selectROI('green2',frame)
roi_yellow=cv2.selectROI('yellow',frame)
roi_white=cv2.selectROI('white',frame)
cv2.destroyAllWindows()

white_bgr=frame[int(roi_white[1]):int(roi_white[1]+roi_white[3]),int(roi_white[0]):int(roi_white[0]+roi_white[2])]
red_bgr=frame[int(roi_red[1]):int(roi_red[1]+roi_red[3]),int(roi_red[0]):int(roi_red[0]+roi_red[2])]
blue_bgr=frame[int(roi_blue[1]):int(roi_blue[1]+roi_blue[3]),int(roi_red[0]):int(roi_red[0]+roi_red[2])]
green_bgr=frame[int(roi_green[1]):int(roi_green[1]+roi_green[3]),int(roi_green[0]):int(roi_green[0]+roi_green[2])]
yellow_bgr=frame[int(roi_yellow[1]):int(roi_yellow[1]+roi_yellow[3]),int(roi_yellow[0]):int(roi_yellow[0]+roi_yellow[2])]
green_bgr_2=frame[int(roi_green_2[1]):int(roi_green_2[1]+roi_green_2[3]),int(roi_green_2[0]):int(roi_green_2[0]+roi_green_2[2])]

white_rmin=white_bgr[:,:,2].min()
white_bmin=white_bgr[:,:,0].min()
white_gmin=white_bgr[:,:,1].min()
blue_rmin=blue_bgr[:,:,2].min()
blue_bmin=blue_bgr[:,:,0].min()
blue_gmin=blue_bgr[:,:,1].min()
green_rmin=green_bgr[:,:,2].min()
green_bmin=green_bgr[:,:,0].min()
green_gmin=green_bgr[:,:,1].min()
yellow_rmin=yellow_bgr[:,:,2].min()
yellow_bmin=yellow_bgr[:,:,0].min()
yellow_gmin=yellow_bgr[:,:,1].min()
green_rmin_2=green_bgr_2[:,:,2].min()
green_bmin_2=green_bgr_2[:,:,0].min()
green_gmin_2=green_bgr_2[:,:,1].min()

red_rmin=red_bgr[:,:,2].min()
red_bmin=red_bgr[:,:,0].min()
red_gmin=red_bgr[:,:,1].min()

white_rmax=white_bgr[:,:,2].max()
white_bmax=white_bgr[:,:,0].max()
white_gmax=white_bgr[:,:,1].max()
blue_rmax=blue_bgr[:,:,2].max()
blue_bmax=blue_bgr[:,:,0].max()
blue_gmax=blue_bgr[:,:,1].max()
green_rmax=green_bgr[:,:,2].max()
green_bmax=green_bgr[:,:,0].max()
green_gmax=green_bgr[:,:,1].max()
green_rmax_2=green_bgr_2[:,:,2].max()
green_bmax_2=green_bgr_2[:,:,0].max()
green_gmax_2=green_bgr_2[:,:,1].max()


yellow_rmax=yellow_bgr[:,:,2].max()
yellow_bmax=yellow_bgr[:,:,0].max()
yellow_gmax=yellow_bgr[:,:,1].max()
red_rmax=red_bgr[:,:,2].max()
red_bmax=red_bgr[:,:,0].max()
red_gmax=red_bgr[:,:,1].max()
'''
white,blue,gren,yellow,red
'''
thresh_value=np.array([[[white_bmin,white_gmin,white_rmin],[blue_bmin,blue_gmin,blue_rmin],[min(green_bmin,green_bmin_2),min(green_gmin,green_gmin_2),min(green_rmin,green_rmin_2)],[yellow_bmin,yellow_gmin,yellow_rmin],[red_bmin,red_gmin,red_rmin]]]+[[[white_bmax,white_gmax,white_rmax],[blue_bmax,blue_gmax,blue_rmax],[max(green_bmax,green_bmax_2),max(green_gmax,green_gmax_2),max(green_rmax,green_rmax_2)],[yellow_bmax,yellow_gmax,yellow_rmax],[red_bmax,red_gmax,red_rmax]]])

print('calculating number of white boxes on green in the starting')
array,green_matrix=input_array(frame,roi,thresh_value)
count_green=np.where(green_matrix==6)
count_green=list(zip(count_green[0],count_green[1]))
white_box=np.where(array==0)
white_box=list(zip(white_box[0],white_box[1]))
count_horuxes=0
for x in white_box:
    for y in count_green:
        if(x==y):
            count_horuxes+=1
            break
flag_leave=0
flag_corner=0
while True:
    ser.write(b'A')
    #taking inputs
    _,frame=cap.read()
    
    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
    rows,cols=frame.shape[:2]
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    corners,current_pos,_=aruco_marker(frame,roi)
    #algorithm
    array,green_matrix=input_array(frame,roi,thresh_value)
    count_green=np.where(green_matrix==6)
    count_green=list(zip(count_green[0],count_green[1]))
    count_blue=np.where(array==5)
    count_blue=list(zip(count_blue[0],count_blue[1]))
    count_blue=len(count_blue)
    count_white=np.where(array==0)
    count_white=list(zip(count_white[0],count_white[1]))
    count_green_white=0
    for x in white_box:
        for y in count_green:
            if(x==y):
                count_green_white+=1
                break
    if (count_blue==1) or (count_green_white==0):
        print('count_green_white ==0 or count_blue ==1')
        done2=1
        while True:
            ser.write(b'A')
            array,_=input_array(frame,roi,thresh_value)
            white_box=np.where(array==0)
            white_box=list(zip(white_box[0],white_box[1]))
            count_green=np.where(green_matrix==6)
            count_green=list(zip(count_green[0],count_green[1]))

            print('preparing for left out green box where white box is still there')
            print('going for non corner white box')
            count_blue=np.where(green_matrix==5)
            count_blue=list(zip(count_blue[0],count_blue[1]))

            for x in white_box:
                for y in count_green:
                    if(x!=y)and(x!=count_blue[0])and(x!=count_blue[1])and(x!=count_blue[2])and(x!=count_blue[3])and(x!=count_blue[4])and(x!=flag_leave) :
                        done=True
                        corners,current_pos,_=aruco_marker(frame,roi)
                        path=djikstras(current_pos,x,array)
                        break
                if done:
                    break
            
            pathFolllower(frame,path,current_pos,roi)
            ser.write(b'G')
            time.sleep(5)
            ser.write(b'S')
            ser.write(b'R')
            ser.write(b'O')
            time.sleep(2)
            ser.write(b'S')
            print('seeing the colour below')
            _,frame=cap.read()
            frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
            corners,current_pos,_=aruco_marker(frame,roi)
            array,_=input_array(frame,roi,thresh_value)
            print('working on the destination')
            des_colour=array[x[0]][x[1]]
            count_green=np.where(green_matrix==6)
            count_green=list(zip(count_green[0],count_green[1]))
            count_loop=0
            for y in count_green:
                if (array[y[0]][y[1]]==des_colour):
                    path=djikstras(current_pos,[y[0],y[1]],array,extension=1,min_colour=des_colour)
                    pathFolllower(frame,path,current_pos,roi)
                    ser.write(b'A')
                    time.sleep(5)
                    ser.write(b'S')
                    ser.write(b'P')
                    time.sleep(2)
                    ser.write(b'S')
                else:
                    count_loop+=1
                
            print('if no destinaton matches moving on to other white box')
            if(count_loop==4):
                print('preparing for the case if none of the corners has the shape which is hidden under white') 
                print('along with the corner')
                for y in white_box:
                    for z in count_green:
                        if(y==z):
                            flag_corner=y
                flag_colour=des_colour
                flag_leave=x
                ser.write(b'L')
                time.sleep(2)
                ser.write(b'S')
                ser.write(b'A')
                time.sleep(5)
                ser.write(b'S')
            _,frame=cap.read()
            frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
            array,_=input_array(frame,roi,thresh_value)
            white_box=np.where(array==0)
            white_box=list(zip(white_box[0],white_box[1]))

            count_white=0
            for x in white_box:
                for y in count_green:
                    if(x!=y)and(x!=[4,4])and(x!=[8,3])and(x!=[8,4])and(x!=[8,5]) :
                        count_white+=1
            
            if(count_white==1) and (flag_corner!=0):
                print('working on last white box')
                print('going for non corner white box')
                count_blue=np.where(green_matrix==5)
                count_blue=list(zip(count_blue[0],count_blue[1]))

                for x in white_box:
                    for y in count_green:
                        if(x!=y)and(x!=count_blue[0])and(x!=count_blue[1])and(x!=count_blue[2])and(x!=count_blue[3])and(x!=count_blue[4]) :
                            done=True
                            corners,current_pos,_=aruco_marker(frame,roi)
                            path=djikstras(current_pos,x,array)
                            break
                    if done:
                        break
                
                pathFolllower(frame,path,current_pos,roi)
                ser.write(b'G')
                time.sleep(5)
                ser.write(b'S')
                ser.write(b'R')
                ser.write(b'O')
                time.sleep(2)
                ser.write(b'S')
                print('seeing the colour below')
                _,frame=cap.read()
                frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                corners,current_pos,_=aruco_marker(frame,roi)
                array,_=input_array(frame,roi,thresh_value)
                print('working on the destination')
                des_colour=array[x[0]][x[1]]
                count_green=np.where(green_matrix==6)
                count_green=list(zip(count_green[0],count_green[1]))
                count_loop=0

                count_green=np.where(green_matrix==6)
                count_green=list(zip(count_green[0],count_green[1]))
                count_loop=0
                for y in count_green:
                    #here
                    if (array[y[0]][y[1]]==des_colour):
                        path=djikstras(current_pos,[y[0],y[1]],array,extension=1,min_colour=des_colour)
                        pathFolllower(frame,path,current_pos,roi)
                        ser.write(b'A')
                        time.sleep(5)
                        ser.write(b'S')
                        ser.write(b'P')
                        time.sleep(2)
                        ser.write(b'S')
                        _,frame=cap.read()
                        frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                        corners,current_pos,_=aruco_marker(frame,roi)
                        path=djikstras(current_pos,flag_corner,array)
                        pathFolllower(frame,path,current_pos,roi)
                        ser.write(b'G')
                        time.sleep(5)
                        ser.write(b'S')
                        _,frame=cap.read()
                        frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                        count_blue=np.where(array==5)
                        count_blue=list(zip(count_blue[0],count_blue[1]))
                        for x in count_blue:
                            break
                        corners,current_pos,_=aruco_marker(frame,roi)
                        path=djikstras(current_pos,x,array)
                        pathFolllower(frame,path,current_pos,roi)
                        ser.write(b'L')
                        time.sleep(5)
                        ser.write(b'S')
                        ser.write(b'Q')
                        time.sleep(2)
                        ser.write(b'S')
                        done2=0
                        break
                    else:
                        count_loop+=1
                    
                #if no destinaton matches moving on to other white box
                if(count_loop==4):

                
                    _,frame=cap.read()
                    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                    corners,current_pos,_=aruco_marker(frame,roi)
                    path=djikstras(current_pos,flag_corner,array)
                    pathFolllower(frame,path,current_pos,roi)
                    ser.write(b'G')
                    time.sleep(5)
                    ser.write(b'S')
                    _,frame=cap.read()
                    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                    count_blue=np.where(array==5)
                    count_blue=list(zip(count_blue[0],count_blue[1]))
                    for x in count_blue:
                        break
                    corners,current_pos,_=aruco_marker(frame,roi)
                    path=djikstras(current_pos,x,array)
                    pathFolllower(frame,path,current_pos,roi)
                    ser.write(b'L')
                    time.sleep(5)
                    ser.write(b'S')
                    ser.write(b'Q')
                    time.sleep(2)
                    ser.write(b'S')
                    
                    _,frame=cap.read()
                    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                    corners,current_pos,_=aruco_marker(frame,roi)
                    path=djikstras(current_pos,flag_leave,array)
                    pathFolllower(frame,path,current_pos,roi)
                    ser.write(b'G')
                    time.sleep(5)
                    ser.write(b'O')
                    ser.write(b'S')
                    _,frame=cap.read()
                    frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
                    corners,current_pos,_=aruco_marker(frame,roi)
                    path=djikstras(current_pos,flag_corner,array,extension=1,min_colour=flag_colour)
                    pathFolllower(frame,path,current_pos,roi)
                    ser.write(b'L')
                    time.sleep(5)
                    ser.write(b'S')
                    ser.write(b'P')
                    time.sleep(2)
                    ser.write(b'S')
                    done2=0
                    break
            if(done2==0):
                break

                
    #to take the corner 3 boxes to the blue places
    else:
        
        #calulating the corner to go to pick up the white box and keep it at blue
        corners,current_pos,_=aruco_marker(frame,roi)
        min_dis=np.inf
        white_box=np.where(array==0)
        white_box=list(zip(white_box[0],white_box[1]))
        green_matrix=np.where(green_matrix==6)
        green_matrix=list(zip(green_matrix[0],green_matrix[1]))
        for corner_img in white_box:
            for y in green_matrix:
                if(corner_img==y):
                    norm=[y[0]-current_pos[0],y[1]-current_pos[1]]
                    norm=math.sqrt(norm[0]*norm[0]+norm[1]*norm[1])
                    if(min_dis>norm):
                        min_dis=norm
                        final_pos=corner_img
                    break
        
        path=djikstras(current_pos,final_pos,array)
        pathFolllower(frame,path,current_pos,roi)
        #grabs the box
        ser.write(b'G')
        time.sleep(5)
        ser.write(b'S')
        #calculating an taking the first white corner box to blue
        _,frame=cap.read()
        frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
        _,current_pos,_=aruco_marker(frame,roi)
        blue_destination=np.where(array==5)
        blue_destination=list(zip(blue_destination[0],blue_destination[1]))
        while(len(blue_destination)<=1):
            blue_destination=np.where(array==5)
            blue_destination=list(zip(blue_destination[0],blue_destination[1]))
            if(len(blue_destination)>=2):
                break
            
        if(blue_destination[0]==[5,5]):
            _,frame=cap.read()
            frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
            corners,current_pos,_=aruco_marker(frame,roi)
            path=djikstras(current_pos,blue_destination[1],array)
            pathFolllower(frame,path,current_pos,roi)
        else:
            _,frame=cap.read()
            frame=frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
            corners,current_pos,_=aruco_marker(frame,roi)
            path=djikstras(current_pos,blue_destination[0],array)
            pathFolllower(frame,path,current_pos,roi)
        ser.write(b'L')
        time.sleep(5)
        ser.write(b'S')
        ser.write(b'Q')
        time.sleep(2)
        ser.write(b'S')
print('PS solved')
cv2.destroyAllWindows()
cap.release()
ser.close()
