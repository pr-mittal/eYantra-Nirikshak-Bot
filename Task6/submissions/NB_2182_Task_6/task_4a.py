'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 4A of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			2182
# Author List:		Aman Kumar,Pranav Mittal
# Filename:			task_4a.py
# Functions:		find_path, read_start_end_coordinates,make_step,getMinPath,getPath
# 					[ Comma separated list of functions in this file ]
#                     
# Global variables:	
# 					[ List of global variables defined in this file ]
                    
####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the six available   ##
## modules for this task (numpy, opencv, os, traceback,     ##
## sys, json)												##
##############################################################
import numpy as np
import cv2
import os
import traceback
import sys
import json


# Import 'task_1b.py' file as module
try:
    import task_1b

except ImportError:
    print('\n[ERROR] task_1b.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_1b.py is present in this current directory.\n')
    sys.exit()

except Exception as e:
    print('Your task_1b.py throwed an Exception, kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)
    sys.exit()

##############################################################


# In[9]:


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
# """
# we shall find the path by using the fact that each row adjacent to given row must have just one unit difference
# """
def make_step(k, distance_mat, maze_array):
    '''
    Purpose:
    ---
    take a step in the distance_mat,i.e start to tranverse the map(distance_mat) further using maze_array
    Input Arguments:
    'k':[integer]
        the distance from the start position that we have reached
    ' distance_mat':[list]
        list of distance matrix i.e map of the maze , it has the min distance of each coordinate from the start
    ' maze_array':[list]
        list of maze array
    ---
    Returns:
    ---
    'distance_mat':[list]
        map of the maze after traversing one step if possible in all directions
    Example call:
    ---
    distance_mat=make_step(k, distance_mat, maze_array)
    '''
    for i in range(10):
        for j in range(10):  
            # print(distance_mat[i][j]==k)
            if distance_mat[i][j]==k:
                #from node at which is at distance k form start
                #we explore which all directions are possible and store k+1 there
                
                # print(distance_mat[i][j]==k) 

                l= maze_array[i][j]
                # print(l)
                # print(i)
                # print("aman")
                #WEST
                if (l%2==0) and distance_mat[i][j-1]==0:
                    distance_mat[i][j-1]=k+1
                
                l=(int)(l/2)
                # print (l)
                
                #NORTH
                if (l%2==0) and distance_mat[i-1][j]==0:
                    distance_mat[i-1][j]= k+1
                l=(int)(l/2)
                # print (l)
                
                #EAST
                if (l%2==0) and distance_mat[i][j+1]==0:
                    distance_mat[i][j+1]=k+1
                l=(int)(l/2)
                # print (l)
                
                #SOUTH
                if (l%2==0) and distance_mat[i+1][j]==0:
                    distance_mat[i+1][j]=k+1
                # print(distance_mat)
                
    return distance_mat

# """
# we might have multiple paths from start to end
# we see that which path has least corners and sotre just the corners in the path
# we return the path that has min corners and return that as output
# """
def getMinPath(path):
    '''
    Purpose:
    ---
    get the minimum path from all the paths that were calculated after depth first search

    Input Arguments:
    ---
    'path':[list]
        list of all the posiible path from start to the end
    Returns:
    ---
    'minPath':[list]
    list of tupes of coordinates fo path , that has minimum corners
    Example call:
    ---
    min_path=getMinPath(path)
    '''
    path_copy=[]
    #print(path)
    #print(path[0])
    #looping through all the possible paths that we got via traversal in find_path
    #see the path that has least corners
    for m in range(len(path)):
        path_copy+=[path[m].copy()]
        #storing the previos index
        prev_x=-1
        #count the number of x that have had the same value as x, till present existing in the path
        #if count=1 and x==prev_x,meaning now 3 consecutive times x has been same
        #we delete the prev_node , so the cnt stays 1
        cnt_x=0#number of x that have been common
        prev_y=-1
        cnt_y=0
        #print(prev_x,prev_y)
        n=len(path[m])
        i=0
        while(i<n):
    
            x=path[m][i][0]
            y=path[m][i][1]
            #see if there are coordinates such that x are same in continuation
            if(x==prev_x):
                if(cnt_x==1):
                    #remove the coodrdinate before
                    #as this coordinate(x,y) and (prev_prev_x,prev_prev_y) are sufficient for this line
                    #print(path[m])
                    #print((prev_x,prev_y))
                    #print("deleted ",prev_x," ",prev_y)
                    path[m].remove((prev_x,prev_y))
                    i-=1#we dont want ncrement in i so to neutralise i+=1 in future
                else:
                    cnt_x=1#if x is same and xnt_x==0, cnt_x=1 , for next time
            else:
                cnt_x=0#if x are not same
                
            #see if there are coordinates such that y are same in continuation
            #for documentation see x above
            if(y==prev_y):
                if(cnt_y==1):
                    #more 
                    #remove the coodrdinate before
                    #print("deleted ",prev_x," ",prev_y)
                    path[m].remove((prev_x,prev_y))
                    i-=1
                else:
                    cnt_y=1
                
            else:
                cnt_y=0
            #storing the previous coordinates
            prev_x=x
            prev_y=y
            i+=1#moving to the next node
            n=len(path[m])#as we keep on deleting the nodes , we need to update the n
            #print(x," ",y," ",cnt_x," ",cnt_y)
            
    #check which path has min coordinate/corners left,will run the fastest pid
    min_c=len(path[0])
    min_indx=0
    for i in range(len(path)):
        if(min_c>len(path[i])):
            min_c=len(path[i])
            min_indx=i
    #print(path[min_indx])
    #print(path,path_copy)
    return path_copy[min_indx]

#"""
#---Just some extra test cases for checking 
#"""
# removeExtraPnts([[(0, 4), (1, 4), (1, 3), (1, 2), (2, 2), (2, 1), (3, 1),
#         (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
#         (3, 7), (3, 6), (3, 5), (3, 4), (2, 4), (2, 5), (1, 5),
#         (1, 6), (2, 6), (2, 7), (2, 8), (3, 8), (4, 8), (5, 8),
#         (6, 8), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3),
#         (5, 2), (6, 2), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4),
#         (6, 4), (6, 5), (7, 5), (7, 6), (7, 7), (7, 8), (8, 8),
#         (8, 7), (8, 6), (8, 5), (9, 5)]]);
# [(0, 4), (1, 4), (1, 2),(2,2), (2, 1),
# (4, 1), (4, 7),
# (3, 7), (3, 4), (2, 4), (2, 5), (1, 5),
# (1, 6), (2, 6), (2, 8),
# (6, 8), (6, 7), (5, 7),
# (5, 2), (6, 2), (6, 1), (7, 1), (7, 4),
# (6, 4), (6, 5), (7, 5), (7, 8), (8, 8),
# (8, 5), (9, 5)]


# In[10]:


# """
# it returns the path , traversing from end_coord to start_cood using recursion
# """
def getPath(start_coord,end_coord,distance_mat,maze_array):
    '''
    Purpose:
    ---
    Traverse staarting from last node to start coord , using recursion andthus we will have the path

    Input Arguments:
    ---
    'start_coord':[tuple]
        start coordinate from ehich we are tracing back,i.e. that has disatance one lestt than this node
    'end_coord':[tuple]
        the destination we are aiming for
    'distance_mat':[list]
        the map of paths useful maze used to traverse back
    'maze_array':[list]
        the maze array
    Returns:
    ---
    final_pat:[list]
    list of all the possible paths from start_coord to end_coord
    Example call:
    ---
    final_path=getPath(start_coord,end_coord,distance_mat,maze_array)
    '''
    #print(end_coord)
    #path making
    i,j =end_coord
    k =distance_mat[i][j]
    #print(end_coord,start_coord)
    
    #breaking the traversal when we reach the start_coord
    if(end_coord==start_coord):
        #print("END=START")
        return [[]]
    #while k > 1:
    #count for multiple paths from a point possible
    #that is more than if here become true
    #so we use recursion
    final_path=[]
    
    l=maze_array[i][j]
    
    ways=0
    #print(maze_array[i][j])
    path_a=[None,None,None,None]
    
    
    #traverasal from end_coord in each direction
    #WEST
    if j>0 and distance_mat[i][j-1]== k-1 and l%2==0:
        #if it is possible to go in that direction we move
        #i, j= i, j-1
        #print("WEST",k-1)
        path_a[0]=getPath(start_coord,(i,j-1),distance_mat,maze_array)
        #if path_a[x] returns None, if after traversal there was no possibility to reach the start_coord
        if(path_a[0]!=None):
            #the path_a[x] is contains all the possible paths,we loop through all of them
            #add a node to each possible path
            for m in range(len(path_a[0])):
                final_path=final_path+[path_a[0][m]+[(i,j-1)]]
            ways+=1
    l=(int)(l/2)
    #NORTH
    #for documentation see 'WEST'
    #print(i-1,j,k-1,distance_mat[i-1][j])
    #print(distance_mat[i-1][j]== k-1)
    #print(l,l%2==0)
    #print(i>0)
    if i>0 and distance_mat[i-1][j]== k-1 and l%2==0:
        #i, j= i-1, j
        #print("NORTH",k-1)
        path_a[1]=getPath(start_coord,(i-1,j),distance_mat,maze_array)
        if(path_a[1]!=None):
            for m in range(len(path_a[1])):
                final_path=final_path+[path_a[1][m]+[(i-1,j)]]
            ways+=1
        #print(path_m1)
    
    l=(int)(l/2);
    #EAST
    #for documentation see 'WEST'
    if j<len(distance_mat)-1 and distance_mat[i][j+1]== k-1 and l%2==0:
        #i, j= i, j+1
        #print("EAST",k-1)
        path_a[2]=getPath(start_coord,(i,j+1),distance_mat,maze_array)
        if(path_a[2]!=None):
            for m in range(len(path_a[2])):
                final_path=final_path+[path_a[2][m]+[(i,j+1)]]
            ways+=1
    l=(int)(l/2)
    #SOUTH
    #for documentation see 'WEST'
    if i<len(distance_mat)-1 and distance_mat[i+1][j]== k-1 and l%2==0:
        #i, j= i+1, j
        #print("SOUTH",k-1)
        path_a[3]=getPath(start_coord,(i+1,j),distance_mat,maze_array)
        if(path_a[3]!=None):
            for m in range(len(path_a[3])):
                final_path=final_path+[path_a[3][m]+[(i+1,j)]]
            ways+=1
    
    #if there is no way possible forward we return None, breaks the traversal in the wrong direction
    if(ways==0):
        #print("RETURNING NONE")
        return None
    
    #if the traversal was successful we return final_path, combination of traveral in all four direction(if it is possible)
    return final_path
#"""
#---Just some extra test cases for checking 
#"""
# maze_array=[[3, 10, 10, 14, 7, 11, 10, 10, 10, 6], [5, 11, 2, 2, 12, 3, 2, 10, 14, 5], [5, 3, 12, 5, 3, 12, 9, 10, 6, 5], [5, 5, 11, 12, 9, 10, 10, 6, 5, 13], [13, 1, 10, 10, 10, 10, 10, 12, 1, 14], [11, 12, 3, 2, 10, 10, 10, 6, 5, 7], [7, 3, 12, 13, 3, 6, 11, 8, 12, 5], [5, 1, 10, 10, 12, 9, 10, 10, 6, 5], [5, 9, 14, 11, 10, 2, 10, 10, 12, 5], [9, 10, 10, 10, 14, 13, 11, 10, 10, 12]]
# start_coord=[0, 4]
# end_coord=[9, 5]
# distance_mat=[[ 0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0],
#  [ 0  ,5  ,4  ,3  ,2 ,21 ,22 ,23 ,24  ,0],
#  [ 0  ,6  ,5  ,4 ,19 ,20 ,23 ,24 ,25  ,0],
#  [ 0  ,7  ,6  ,5 ,18 ,17 ,16 ,15 ,26  ,0],
#  [ 0  ,8  ,9 ,10 ,11 ,12 ,13 ,14 ,27 ,28],
#  [10  ,9 ,36 ,35 ,34 ,33 ,32 ,31 ,28  ,0],
#  [ 0 ,38 ,37 ,36 ,43 ,44 ,31 ,30 ,29  ,0],
#  [ 0 ,39 ,40 ,41 ,42 ,45 ,46 ,47 ,48  ,0],
#  [ 0 ,40 ,41  ,0 ,53 ,52 ,51 ,50 ,49  ,0],
#  [ 0  ,0  ,0  ,0  ,0 ,53  ,0  ,0  ,0  ,0]]
# distance_mat=[[ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#  [ 0, 0, 4, 3, 2,21,22, 23,24, 0],
#  [ 0, 6, 5, 0,19,20,23,24,25, 0],
#  [ 0, 7, 0, 0,18,17,16,15,26, 0],
#  [ 0, 8, 9,10,11,12,13,14,27, 0],
#  [ 0,0 ,36,35,34,33,32,31,28, 0],
#  [ 0,38,37, 0,43,44, 0,30,29, 0],
#  [ 0,39,40,41,42,45,46,47,48, 0],
#  [ 0, 0, 0, 0, 0,52,51,50,49, 0],
#  [ 0, 0, 0, 0, 0,53, 0, 0, 0, 0]]
# print(len(distance_mat))
# for i in distance_mat:
#     print(len(i))
# path=getPath(start_coord,end_coord,distance_mat,maze_array)
# print(path)
##############################################################


# In[11]:


def find_path(maze_array, start_coord, end_coord):
    
    """
    Purpose:
    ---
    Takes a maze array as input and calculates the path between the
    start coordinates and end coordinates.

    Input Arguments:
    ---
    `maze_array` :   [ nested list of lists ]
        encoded maze in the form of a 2D array

    `start_coord` : [ tuple ]
        start coordinates of the path

    `end_coord` : [ tuple ]
        end coordinates of the path

    Returns:
    ---
    `path` :  [ list of tuples ]
        path between start and end coordinates

    Example call:
    ---
    path = find_path(maze_array, start_coord, end_coord)
    """

    path = None

    ################# ADD YOUR CODE HERE #################
    row,col=(10,10)
    #here we created a 2d matrix with all rows and cols equal to 0
    distance_mat=np.zeros([row,col], dtype = int) 

    i,j=start_coord
    distance_mat[i][j]=1
    #print(distance_mat)
    
    #navigate from start to end point,storing distance in distance_mat
    k=0
    while distance_mat[end_coord[0]][end_coord[1]]==0:
        k=k+1

        distance_mat=make_step(k, distance_mat,maze_array)
        if(k>101):
            #if k>101 i.e we have been looping for too uch as max k is 100
            #break as there is no path possible
            return None
    #print(distance_mat,k)
    #return None
    # for row in a:
    # 	print(row)

    #path making
    i,j=end_coord
    
    #returns all possible paths fron start_cood to end_coord
    path=getPath(start_coord,end_coord,distance_mat,maze_array)
    if(path==None):
        #if path==None i.e. no path was found
        return None
    
    #from each path the end_coordinate is missing
    for m in range(len(path)):
        #add end coordinate to all paths
        path[m]+=[(end_coord[0],end_coord[1])]
        
    #print(path)
    #segregate extra paths that are of least corners
    path=getMinPath(path)
    
    #print(len(path))
    ######################################################

    return path
# """
# ---Just some extra test cases for checking 
# """
# maze_array=[[3, 10, 10, 14, 7, 11, 10, 10, 10, 6], [5, 11, 2, 2, 12, 3, 2, 10, 14, 5], [5, 3, 12, 5, 3, 12, 9, 10, 6, 5], [5, 5, 11, 12, 9, 10, 10, 6, 5, 13], [13, 1, 10, 10, 10, 10, 10, 12, 1, 14], [11, 12, 3, 2, 10, 10, 10, 6, 5, 7], [7, 3, 12, 13, 3, 6, 11, 8, 12, 5], [5, 1, 10, 10, 12, 9, 10, 10, 6, 5], [5, 9, 14, 11, 10, 2, 10, 10, 12, 5], [9, 10, 10, 10, 14, 13, 11, 10, 10, 12]]
# start_coord=[0, 4]
# end_coord=[9, 5]
# maze_array=[[3, 10, 10, 14, 7, 11, 10, 10, 10, 6], [5, 3, 6, 11, 0, 6, 11, 2, 14, 5], [4, 5, 9, 6, 5, 9, 6, 9, 6, 5], [4, 5, 7, 5, 5, 3, 12, 3, 4, 13], [12, 5, 5, 9, 12, 5, 3, 12, 1, 14], [10, 12, 1, 6, 3, 12, 5, 3, 12, 7], [6, 7, 5, 9, 12, 3, 12, 9, 6, 5], [4, 5, 5, 3, 6, 5, 3, 14, 5, 5], [5, 9, 8, 12, 9, 4, 9, 10, 12, 5], [9, 10, 10, 10, 14, 13, 11, 10, 10, 12]]
# start_coord=[0,3]
# end_coord=[9,6]
# maze_array=[[3, 10, 2, 2, 14, 3, 6, 3, 10, 6], [9, 14, 5, 13, 11, 12, 9, 12, 3, 12], [3, 6, 5, 3, 10, 6, 3, 10, 12, 7], [5, 9, 12, 9, 6, 9, 12, 3, 10, 4], [1, 10, 2, 14, 5, 7, 3, 8, 6, 5], [5, 7, 9, 6, 5, 5, 5, 3, 12, 5], [5, 9, 6, 9, 12, 9, 12, 5, 7, 5], [9, 10, 4, 11, 10, 2, 10, 12, 1, 12], [3, 10, 12, 3, 6, 5, 3, 6, 9, 6], [9, 10, 10, 12, 9, 12, 13, 9, 10, 12]]
# start_coord=[0,0]
# end_coord=[9,9]
# maze_array=[[3, 10, 10, 14, 7, 11, 10, 10, 10, 6], [5, 3, 14, 3, 12, 7, 3, 10, 14, 5], [5, 1, 2, 4, 7, 5, 5, 11, 6, 5], [5, 13, 13, 1, 8, 0, 8, 10, 12, 13], [13, 3, 2, 12, 11, 8, 2, 2, 10, 14], [11, 4, 1, 2, 2, 14, 13, 9, 6, 7], [7, 13, 13, 5, 9, 6, 7, 3, 12, 5], [5, 11, 2, 8, 14, 5, 9, 0, 6, 5], [5, 11, 8, 10, 14, 1, 14, 13, 13, 5], [9, 10, 10, 10, 14, 13, 11, 10, 10, 12]]
# start_coord=(9,5)
# end_coord=(0,4)
# path=find_path(maze_array, start_coord, end_coord)
# print(path)
# [(0, 4), (1, 4), (1, 2),(2,2), (2, 1),
# (4, 1), (4, 7),
# (3, 7), (3, 4), (2, 4), (2, 5), (1, 5),
# (1, 6), (2, 6), (2, 8),
# (6, 8), (6, 7), (5, 7),
# (5, 2), (6, 2), (6, 1), (7, 1), (7, 4),
# (6, 4), (6, 5), (7, 5), (7, 8), (8, 8),
# (8, 5), (9, 5)]


# In[12]:


def read_start_end_coordinates(file_name, maze_name):
    """
    Purpose:
    ---
    Reads the corresponding start and end coordinates for each maze image
    from the specified JSON file

    Input Arguments:
    `file_name` :   [ str ]
        name of JSON file

    `maze_name` : [ str ]
        specify the maze image for which the start and end coordinates are to be returned.

    Returns:
    ---
    `start_coord` : [ tuple ]
        start coordinates for the maze image

    `end_coord` : [ tuple ]
        end coordinates for the maze image

    Example call:
    ---
    start, end = read_start_end_coordinates("start_end_coordinates.json", "maze00")
    """

    start_coord = None
    end_coord = None

    ################# ADD YOUR CODE HERE #################
    f=open(file_name,)
    data=json.load(f)
    start_coord=data[maze_name]["start_coord"]
    end_coord=data[maze_name]["end_coord"]
    f.close()
    ######################################################

    return (start_coord[0],start_coord[1]), (end_coord[0],end_coord[1])


# In[13]:


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input and reads the corresponding start and end coordinates for this image from 'start_end_coordinates.json'
# 					file by calling read_start_end_coordinates function. It then applies Perspective Transform
# 					by calling applyPerspectiveTransform function, encodes the maze input in form of 2D array
# 					by calling detectMaze function and finds the path between start, end coordinates by calling
# 					find_path function. It then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					read_start_end_coordinates and find_path functions.
# if __name__ == "__main__":

# 	# path directory of images in 'test_cases' folder
# 	img_dir_path = 'test_cases/'

# 	file_num = 0

# 	maze_name = 'maze0' + str(file_num)

# 	# path to 'maze00.jpg' image file
# 	img_file_path = img_dir_path + maze_name + '.jpg'

# 	# read start and end coordinates from json file
# 	start_coord, end_coord = read_start_end_coordinates("start_end_coordinates.json", maze_name)

# 	print('\n============================================')
# 	print('\nFor maze0' + str(file_num) + '.jpg')
	
# 	# read the 'maze00.jpg' image file
# 	input_img = cv2.imread(img_file_path)

# 	# get the resultant warped maze image after applying Perspective Transform
# 	warped_img = task_1b.applyPerspectiveTransform(input_img)

# 	if type(warped_img) is np.ndarray:

# 		# get the encoded maze in the form of a 2D array
# 		maze_array = task_1b.detectMaze(warped_img)

# 		if (type(maze_array) is list) and (len(maze_array) == 10):

# 			print('\nEncoded Maze Array = %s' % (maze_array))
# 			print('\n============================================')

# 			path = find_path(maze_array, start_coord, end_coord)

# 			if (type(path) is list):

# 				print('\nPath calculated between %s and %s is %s' % (start_coord, end_coord, path))
# 				print('\n============================================')

# 			else:
# 				print('\n Path does not exist between %s and %s' %(start_coord, end_coord))
		
# 		else:
# 			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
# 			exit()
	
# 	else:
# 		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
# 		exit()
	
# 	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

# 	if choice == 'y':

# 		for file_num in range(1,10):

# 			maze_name = 'maze0' + str(file_num)

# 			img_file_path = img_dir_path + maze_name + '.jpg'

# 			# read start and end coordinates from json file
# 			start_coord, end_coord = read_start_end_coordinates("start_end_coordinates.json", maze_name)

# 			print('\n============================================')
# 			print('\nFor maze0' + str(file_num) + '.jpg')
	
# 			# read the 'maze00.jpg' image file
# 			input_img = cv2.imread(img_file_path)

# 			# get the resultant warped maze image after applying Perspective Transform
# 			warped_img = task_1b.applyPerspectiveTransform(input_img)

# 			if type(warped_img) is np.ndarray:

# 				# get the encoded maze in the form of a 2D array
# 				maze_array = task_1b.detectMaze(warped_img)

# 				if (type(maze_array) is list) and (len(maze_array) == 10):

# 					print('\nEncoded Maze Array = %s' % (maze_array))
# 					print('\n============================================')

# 					path = find_path(maze_array, start_coord, end_coord)

# 					if (type(path) is list):

# 						print('\nPath calculated between %s and %s is %s' % (start_coord, end_coord, path))
# 						print('\n============================================')

# 					else:
# 						print('\n Path does not exist between %s and %s' %(start_coord, end_coord))

# 				else:
# 					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
# 					exit()

# 			else:				
# 				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
# 				exit()
	
# 	else:
#		print()

