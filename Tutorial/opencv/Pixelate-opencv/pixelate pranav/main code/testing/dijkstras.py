import cv2
import numpy as np
# part ofdjikstars algorithm
#updates ditance of non visited nodes
'''
changed here =
'''
def updateDistance(current_pos,adjacency_array,parent_array,visited_array,distance_array):
    if(current_pos-1)>=0 and (current_pos%9-1)>=0:
        if ((distance_array[current_pos-1])>=(adjacency_array[current_pos-1][current_pos]+distance_array[current_pos])) and (visited_array[current_pos-1]!=1):
            distance_array[current_pos-1]=adjacency_array[current_pos-1][current_pos]+distance_array[current_pos]
            parent_array[current_pos-1]=current_pos
    if(current_pos+1)<=80 and (current_pos%9+1)<9:
        if (distance_array[current_pos+1])>=(adjacency_array[current_pos+1][current_pos]+distance_array[current_pos]) and (visited_array[current_pos+1]!=1):
            distance_array[current_pos+1]=adjacency_array[current_pos+1][current_pos]+distance_array[current_pos]
            parent_array[current_pos+1]=current_pos
    if(current_pos-9)>=0 and (current_pos/9-1)>=0:
        if distance_array[current_pos-9]>=(adjacency_array[current_pos-9][current_pos]+distance_array[current_pos])  and (visited_array[current_pos-9]!=1):
            distance_array[current_pos-9]=adjacency_array[current_pos-9][current_pos]+distance_array[current_pos]
            parent_array[current_pos-9]=current_pos
    if(current_pos+9)<=80 and (current_pos/9+1)<9:
        if distance_array[current_pos+9]>=(adjacency_array[current_pos+9][current_pos]+distance_array[current_pos])  and (visited_array[current_pos+9]!=1):
            distance_array[current_pos+9]=adjacency_array[current_pos+9][current_pos]+distance_array[current_pos]
            parent_array[current_pos+9]=current_pos
    visited_array[current_pos]=1

#caculated the nodes having min distance in distance_array for which are not visited and then we visit them
def checkMinNonVisited(distance_array,visited_array):
    min_dis=np.inf
    for i in range(81):
        if(min_dis>distance_array[i]) and (visited_array[i]!=1):
            min_dis=distance_array[i]
    countNonVisited=[]
    for i in range(81):
        if (min_dis==distance_array[i]):
            countNonVisited+=[i]
    return countNonVisited
#calculates path based on the parent node starting fron deestination
def pathGenerator(parent_array,j,current_pos):
    #j is the value of destination in range 0 and 80
    path=[j]
    step=j
    while step!=current_pos:
        '''
        changed here
        '''
        step=parent_array[int(step)]
        #changed here
        
        path=[step]+path
        
        '''
        changed here
        '''
    
    return (path)
                
#main function from where all the commands to upper functions are sent
current_pos=[0,0]
final_pos=[8,0]
colour_matrix=[[0,2,4,5,2,3,4,4,3],[0,2,3,3,5,3,1,2,3],[0,2,3,3,6,7,2,1,3],[0,2,3,1,2,3,1,2,3],[0,11,2,4,6,7,8,9],[0,2,3,1,2,3,1,2,3],[0,2,3,1,2,3,1,2,3],[1,2,3,1,2,3,1,2,3]]

extension=1
min_colour=3
visited_array=np.zeros(81,dtype=np.float32)
parent_array=np.full(81,np.inf)
adjacency_array=np.zeros((81,81),dtype=np.float32)
distance_array=np.full(81,np.inf)
path=[]
#current a[i][j]
#check if v=0 for them if yes then go add your d and their go to one that comes out to be min a[i+1][j],a[i-1][j],a[i][j+1],a[i][j-1]
#making adjacency matrix
#let an element be a[i][j]
#then in adjacency matrix a[i][j] is relate with a[i-1][j] if (i-1)>0,a[i+1][j] if (i+1)<9,a[i][j-1] if (j-1)>0,a[i][j+1] if (j+1)<9
for i in range(9):
    for j in range(9):
        if(i-1)>=0:
            adjacency_array[i+j*9][i-1+j*9]=1
            adjacency_array[i-1+j*9][i+j*9]=1
        if(i+1)<9:
            adjacency_array[i+j*9][i+1+j*9]=1
            adjacency_array[i+1+j*9][i+j*9]=1
        if(j-1)>=0:
            adjacency_array[i+j*9][i+(j-1)*9]=1
            adjacency_array[i+(j-1)*9][i+j*9]=1
        if(j+1)<9:
            adjacency_array[i+j*9][i+(j+1)*9]=1
            adjacency_array[i+(j+1)*9][i+j*9]=1

        
#making the shortest path where shapes other than colour_matrix is there
if extension==1:
    find_colour=np.where(colour_matrix==min_colour)[0]
    for i,j in find_colour:
            if(i-1)>=0:
                adjacency_array[i+j*9][i-1+j*9]=0
                adjacency_array[i-1+j*9][i+j*9]=0
            if(i+1)<9:
                adjacency_array[i+j*9][i+1+j*9]=0
                adjacency_array[i+1+j*9][i+j*9]=0
            if(j-1)>=0:
                adjacency_array[i+j*9][i+(j-1)*9]=0
                adjacency_array[i+(j-1)*9][i+j*9]=0
            if(j+1)<9:
                adjacency_array[i+j*9][i+(j+1)*9]=0
                adjacency_array[i+(j+1)*9][i+j*9]=0

white_box=np.where(colour_matrix==0)[0]
for x in white_box:
    visited_array[x[0]+9*x[1]]=1
current_pos=current_pos[0]+current_pos[1]*9
distance_array[current_pos]=0
#j is final destination
j=final_pos[0]+final_pos[1]*9
updateDistance(current_pos,adjacency_array,parent_array,visited_array,distance_array)
while True:
    countNonVisited=checkMinNonVisited(distance_array,visited_array)
    for flag in countNonVisited:
        updateDistance(flag,adjacency_array,parent_array,visited_array,distance_array)
        #changed here
    '''
    changed here
    '''
    if(len(np.where(visited_array==0)[0])==1):
        break
print(parent_array)
print(pathGenerator(parent_array,j,current_pos))
    #ret(path matrix)
