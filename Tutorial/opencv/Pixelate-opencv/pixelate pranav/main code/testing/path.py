#importing liraries
import cv2
import numpy as np
import serial
import time
cap=cv2.VideoCapture(1)
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

# part ofdjikstars algorithm
#updates ditance of non visited nodes
def updateDistance(current_pos,adjacency_array,parent_array,visited_array,distance_array):
    if ((distance_array[current_pos-1])>(adjacency_array[current_pos-1][current_pos]+distance_array[current_pos])) and (visited[current_pos-1]!=1):
        distance_array[current_pos-1]=adjacency_array[current_pos-1][current_pos]+distance_array[current_pos]
        parent_array[current_pos-1]=current_pos
    if (distance_array[current_pos+1])>(adjacency_array[current_pos-+][current_pos]+distance_array[current_pos+1]) and (visited[current_pos+1]!=1):
        distance_array[current_pos+1]=adjacency_array[current_pos+1][current_pos]+distance_array[current_pos]
        parent_array[current_pos+1]=current_pos
    if distance_array[current_pos-9]>(adjacency_array[current_pos-9][current_pos]+distance_array[current_pos-9])  and (visited[current_pos-9]!=1):
        distance_array[current_pos-9]=adjacency_array[current_pos-9][current_pos]+distance_array[current_pos]
        parent_array[current_pos-9]=current_pos
    if distance_array[current_pos+9]>(adjacency_array[current_pos+9][current_pos]+distance_array[current_pos+9])  and (visited[current_pos+9]!=1):
        distance_array[current_pos+9]=adjacency_array[current_pos+9][current_pos]+distance_array[current_pos]
        parent_array[current_pos+9]=current_pos
    visited_array[current_pos]=1

#caculated the nodes having min distance in distance_array for which are not visited and then we visit them
def checkMinNonVisited(distance_array,visited_array):
    min_dis=np.inf
    for i in range(81):
        if(min_dis>distance_array[i]) and (visited_array[i]!=1):
            min_dis=distance_array[i]
    for i inn range(81):
        countNonVisited=[]
        if (min_dis==distance_array[i]):
            countNonVisited+=[i]
    return countNonVisited
#calculates path based on the parent node starting fron deestination
def pathGenerator(parent_array,j):
    #j is the value of destination in range 0 and 80
    path=[]
    step=parent_array[j]
    path=[step]+path
    return path
    
#main function from where all the commands to upper functions are sent
def djikstras(current_pos,final_pos,colour_matrix,extension=0,min_colour=0):
    visited_array=np.zeros(81,dtype=np.uint8)
    parent_array=np.full(81,np.inf)
    adjacency_array=np.zeros((81,81),dtype=np.uint8)
    distance_array=np.full(81,np.inf)
    path=[]
    #current a[i][j]
    #check if v=0 for them if yes then go add your d and their go to one that comes out to be min a[i+1][j],a[i-1][j],a[i][j+1],a[i][j-1]
    #making adjacency matrix
    for i in range(81):
            adjacency_matrix[i+9][i]=1
            adjacency_matrix[i][i+9]=1
            if(i-9>=0):
                adjacency_matrix[i-9][i]=1
                adjacency_matrix[i][i-9]=1
            if(i-1>=0):
                adjacency_matrix[i-1][i]=1
                adjacency_matrix[i][i-1]=1
            adjacency_matrix[i+1][i]=1
            adjacency_matrix[i][i+1]=1

    white_box=np.where(clour_matrix==0)
    #make white boxes unrelated to neighbour
    for x in white_box:
        if(x!=final_pos):
            i=x[0]+9*x[1]
            visited_array[i]=1
    #making the shortest path where shapes other than colour_matrix is there
    if extension==1:
        findcolour=np.where(colour_matrix==count_colour)
        for x in findcolour:
            i=x[0]+9*x[1]
            adjacency_matrix[i+9][i]=0
            adjacency_matrix[i][i+9]=0
            if(i-9>=0)
            adjacency_matrix[i-9][i]=0
            adjacency_matrix[i][i-9]=0
            if(i-1>=0)
            adjacency_matrix[i-1][i]=0
            adjacency_matrix[i][i-1]=0
            adjacency_matrix[i+1][i]=0
            adjacency_matrix[i][i+1]=0

            
        
    
    current_pos=current_pos[0]+current_pos[1]*9
    distance_array[current_pos]=0
    #j is final destination
    j=final_pos[0]+final_pos[1]*9
    updateDistance(current_pos,adjacency_array,parent_array,visited_array,distance_array)
    while current_pos!=j:
        countNonVisited=checkMinNonVisited(distance_array,visited_array)
        for flag in countNonVisited:
            updateDistance(flag,adjacency_array,parent_array,visited_array,distance_array)
    return pathGenerator(parent_array,j)
        #ret(path matrix)
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

    

#align the bot in the start
def align(v1,path):
    v11=np.array([path[0]%9,path[0]/9])
    v2=np.array([path[1]%9,path[1]/9])
    v2=v2-v11
    angle=anglebetween(v1,v2)
    '''
    calibrate the values here
    '''
    if(angle==np.pi):
        ser.write(b'R')
        time.sleep(2)
        ser.write(b'R')
        time.sleep(2)
    if(angle==np.pi/2):
        ser.write(b'R')
        time.sleep(2)
        frame=cap.read()
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _,_,v1=aruco(frame_gray)
        if(anglebetween(v1,v2)==np.pi)
            ser.write(b'R')
            time.sleep(2)
            ser.write(b'R')
            time.sleep(2)
    ser.write(b'F')

#make the bot follow the path as directed
def pathFolllower(frame,path,current_pos):
    #align the bot
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,current_pos,v1=aruco_marker(frame_gray)
    align(v1,path)
    #make the bot follow the path
    for i in range(2,len(path)-1):
        if(path[i]==(current_pos[0]+current_pos[1]*9)):
            ser.write(b'L')
            time.sleep(2)
            ser.write(b'F')
            time.sleep(2)
            
        elif(path[i]==(current_pos[0]+current_pos[1]*9)):
            ser.write(b'F')
            time.sleep(2)
        elif(path[i]==(current_pos[0]+current_pos[1]*9)):
            ser.write(b'R')
            time.sleep(2)
            ser.write(b'F')
            time.sleep(2)

        
    
def input_array(frame):
    #settng up processing values
    input_bgr=frame
    input_gray=cv2.cvtColor(input_bgr,cv2.COLOR_BGR2GRAY)
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
    mask_white=cv2.threshold(input_gray,220,255,cv2.THRESH_BINARY)

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
    cv2.imshow('mask_yellow',mask_yellow)
    ##cv2.imshow('mask_blue',mask_blue)

    #contours
    cnt_red,_=cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt_yellow,_=cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt_blue,_=cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
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
            approx_yellow=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
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
    #make a mask for white and update values after updating values due to blue mask 
    for cnt in cnt_white:
        area=cv2.contourArea(cnt)
        if area>50:
            '''
    check value of 0.05
    '''
            approx_white=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
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
    
    count_blue=len(np.where(output==5))
    
    return output,count_blue

#detection of aruco marker
def aruco_marker(frame,extension=0):
    #arucomarker
    frame_gray=cv2.cvtColor(frame,cv2.BGR2HSV)
    aruco_dict=aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters=aruco.DetectorParameters_create()
    corners,markerIds,_=aruco.detectMarkers(frame_gray,aruco_dict,parameters=parameters)


    M=cv2.moments(corners[0])
    cX=M["m10"]/M["m00"]
    cY=M["m01"]/M["m00"]
    '''
    change 5 to 9
    '''
    current_pos=[int(cX/int(rows/5)),int(cY/int(cols/5))]
    v1=(corners[0][1]+corners[0][2])/2-(corners[0][3]+corners[0][4])/2
    return corners,current_pos,v1
        


#main program starts
flag_count=1
while True:
    #taking inputs
    _,frame=cap.read()
    rows,cols=frame.shape[:2]
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    corners,current_pos,_=aruco_marker(frame)
    #algorithm
    array,count_blue=input_array(frame)
    if (count_blue==1):
        array,_=input_array(frame)
        white_box=np.where(array==0)
        for x in white_box:
            if(x[0]!=0)and(x[0]!=9)and(x[1]!=0)and(x[1]!=9):
                path=djikstras(current_pos,x,array)
                break
        #preparing for the case if none of the corners has the shape which is hidden under white 
        #along with the corner
        if(flag_count==1):
            flag_leave=x
            flag_count++
            for y in white_box:
                if(y[0]==0)||(y[0]==9)||(y[1]==0)||(y[1]==9):
                    flag_corner=y
        pathFolllower(frame,path,current_pos)
        ser.write(b'G')
        time.sleep(5)
        ser.write(b'B')
        time.sleep(2)
        #seeing the colour below
        _,frame=cap.read()
        corners,current_pos,_=aruco_marker(frame)
        array,_=input_array(frame_gray)
        #working on the destination
        des_colour=array[x[0],x[1]]
        if (array[0,0]==des_colour):
                path=djikstras(current_pos,[0,0],array,extension=1,min_colour=des_colour)
                pathFolllower(frame,path,current_pos)
                ser.write(b'L')
                time.sleep(5)
                ser.write(b'O')
                time.sleep(2)
        elif (array[9,0]==des_colour):
                path=djikstras(current_pos,[9,0],array,extension=1,min_colour=des_colour)
                pathFolllower(frame,path,current_pos)
                ser.write(b'L')
                time.sleep(5)
                ser.write(b'O')
                time.sleep(2)
        elif (array[0,9]==des):
                path=djikstras(current_pos,[0,9],array,extension=1,min_colour=flag_corner)
                pathFolllower(path,current_pos)
                ser.write(b'L')
                time.sleep(5)
                ser.write(b'O')
                time.sleep(2)
        elif (array[9,9]==des):
            path=djikstras(current_pos,[9,9],array,extension=1,min_colour=flag_corner)
            pathFolllower(path,current_pos)
                ser.write(b'L')
                time.sleep(5)
                ser.write(b'O')
                time.sleep(2)
        #if no destinaton matches moving on to other white box
        elif:
            flag_colour=des_colour
            ser.write(b'F')
            time.sleep(2)
            ser.write(b'L')
            time.sleep(5)
            for y in white_box:
            if(y[0]!=0)and(y[0]!=9)and(y[1]!=0)and(y[1]!=9)and(y!=flag_leave):
                path=djikstras(current_pos,y,array)
                break
            ser.write(b'G')
            time.sleep(5)
            ser.write(b'B')
            time.sleep(2)
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            array,_=input_array(frame)
            des_colour=array[x[0],x[1]]
            if (array[0,0]==des_colour):
                    path=djikstras(current_pos,[0,0],array,extension=1,min_colour=des_colour)
                    pathFolllower(frame,path,current_pos)
                    ser.write(b'L')
                    time.sleep(5)
                    ser.write(b'O')
                    time.sleep(2)
            if (array[9,0]==des_colour):
                    path=djikstras(current_pos,[9,0],array,extension=1,min_colour=des_colour)
                    pathFolllower(frame,path,current_pos)
                    ser.write(b'L')
                    time.sleep(5)
                    ser.write(b'O')
                    time.sleep(2)
            if (array[0,9]==des_colour):
                    path=djikstras(current_pos,[0,9],array,extension=1,min_colour=des_colour)
                    pathFolllower(frame,path,current_pos)
                    ser.write(b'L')
                    time.sleep(5)
                    ser.write(b'O')
                    time.sleep(2)
            elif (array[9,9]==des_colour):
                    path=djikstras(current_pos,[9,9],array,extension=1,min_colour=des_colour)
                    pathFolllower(frame,path,current_pos)
                    ser.write(b'L')
                    time.sleep(5)
                    ser.write(b'O')
                    time.sleep(2)
        x=np.where(array[1:7,1:7]==0)
        if(len(x)==1):
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            path=djikstras(current_pos,flag_corner,array)
            pathFolllower(frame,path,current_pos)
            ser.write(b'G')
            time.sleep(5)
            pos_blue=np.where(array[0:8,0:8]==5)
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            path=djikstras(current_pos,pos_blue,array)
            pathFolllower(frame,path,current_pos)
            ser.write(b'L')
            time.sleep(5)
            ser.write(b'P')
            time.sleep(2)
            
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            path=djikstras(current_pos,flag_leave,array)
            pathFolllower(frame,path,current_pos)
            ser.write(b'G')
            time.sleep(5)
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            path=djikstras(current_pos,flag_corner,array,extension=1,min_colour=flag_colour)
            pathFolllower(frame,path,current_pos)
            ser.write(b'L')
            time.sleep(5)
            ser.write(b'O')
            time.sleep(2)
            ser.write(b'S')
            break

            
                
    elif(count_blue>1):
        
        #calulating the corner to go to pick up the white box and keep it at blue
        min_dis=np.inf
        white_box=np.where(array==0)
        for corner_img in white_box:
            if(corner_img==[0,0]) or (corner_img==[9,9]) or (corner_img==[9,0]) or (corner_img==[0,9]): 
                norm=cv2.norm(current_pos-corner_img)
                if(min_dis>norm):
                    final_pos=corner_img
        path=djikstras(current_pos,corner_img,array_first)
        pathFollower(frame,path,current_pos)
        #grabs the box
        ser.write(b'G')
        time.sleep(5)
        #calculating an taking the first white corner box to blue
        frame=cap.read()
        _,current_pos,_=aruco(frame)
        blue_destination=np.where(array==5)

        if(blue_destiantion[0]==[5,5]):
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            path=djikstras(current_pos,blue_destination[1],array_first)
        else:
            _,frame=cap.read()
            corners,current_pos,_=aruco_marker(frame)
            path=djikstras(current_pos,blue_destination[0],array_first)
            pathFolllower(path,current_pos)
        ser.write(b'L')
        time.sleep(5)
        ser.write(b'P')
        time.sleep(2)
cv2.destroyAllWindows()
cap.release()
