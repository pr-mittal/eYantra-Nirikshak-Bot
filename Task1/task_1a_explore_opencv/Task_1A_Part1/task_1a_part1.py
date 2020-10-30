#!/usr/bin/env python
# coding: utf-8

# In[55]:


'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Author List:		Pranav Mittal,Priyank Sisodia,Aman Sharma,Yatharth Bhargava
# Filename:			task_1a_part1.py
# Functions:		scan_image
# 					getContours,getShape4,isEqual,isPerpendicular
# Global variables:	shapes
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
#import matplotlib.pyplot as plt
##############################################################


# In[56]:


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
#------------------------------------------------------------------------------------------------------
#function to get contours
def getContours(img,imgColor):
    #makes countours in the image and tells the color
    global shapes
    imgHsv=cv2.cvtColor(imgColor,cv2.COLOR_BGR2HSV)
    contours, heirarchy =  cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))
    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt,True) #it gives the perimeter of each shape(true is for closed shape)
        approxCnt = cv2.approxPolyDP(cnt,0.01*perimeter,True) #this will give coridinates of all the corner points
        
        #imgColor = cv2.polylines(imgColor, approxCnt,  True, 0, 10)
        #using moments
        #contour on image--#img   #countour #index #color #thickness
        #print(img.shape[0]*img.shape[1]-100000)
        if area>500 and area<0.9*img.shape[0]*img.shape[1]: #to avoid the noise in the image
            #print("farea =",area) #print area
            #cv2.drawContours(imgColor,approxCnt,-1,(255,0,0),3)#index =-1 means all the countours
            #print("fCorners =",len(approxCnt)) #this will print number of corneres in each cotour
            n_corners = len(approxCnt)
            #now we will draw a rounded box around the detected object(or shape)
            #x, y, w, h = cv2.boundingRect(approxCnt) #this function takes the corners cordinates of shape and returns the x,y,width,hight of the bounding box(x,y are top left corner cordinate)
            #cv2.rectangle(imgColor,(x,y),(x+w,y+h),(0,0,255),5) #draw a bounding rect with the corinates we got (x,y)=tope left,(x+w,y+h)=right bottom corner
            #imgColor = cv2.polylines(imgColor, approxCnt,  True, 0, 10) 
            #=============================================================================================
            #for detection of shape
            #Circle/ Triangle/ Trapezium/ Rhombus/ Square/ Quadrilateral/ Parallelogram/ Pentagon/ Hexagon
            if n_corners>6:
                obj="Circle"
            elif n_corners ==3:
                obj = "Triangle"    
            elif n_corners ==5:
                obj = "Pentagon"
            elif n_corners ==6:
                obj = "Hexagon"
            elif n_corners ==4:
                obj=getShape4(approxCnt)
            #print("fshape =",obj) #print shape
            #cv2.putText(img,obj,(x+(w//2)-60,y+(h//2)-5),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,0,0),2)
            #for centroid
            M = cv2.moments(approxCnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            #print(f"centroid = ",(cX,cY)," Object=",obj) #print centroid
            #cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            #print(imgT[cY,cX])
            ##color detection
            h = imgHsv[cY,cX][0]
            #print(h)
            if (h<=25 and h>=0 )or(h<=180 and h>=175) :
                color ="red"
            elif h<=70 and h>=35 :
                color ="green"
            elif h<=145 and h>=90 :
                color ="blue"
            else:
                color ="unknown"
            #print(img[cY,cX])
            #print(f"centroid = ",(cX,cY)," Object=",obj," color=",color)
            #print("==================================")
            shapes[obj]=[color,area,cX,cY]
    #plt.imshow(cv2.cvtColor(imgColor,cv2.COLOR_BGR2RGB))
    return shapes
    ##till now it will draw all the contours in the image
    #print(imgT[cX][cY])


# In[57]:


def getShape4(cnt):
    #print(cnt)
    #Trapezium/ Rhombus/ Square/ Quadrilateral/ Parallelogram
    obj = "Quadrilateral"
    v1=[cnt[0][0][0]-cnt[1][0][0],cnt[0][0][1]-cnt[1][0][1]]
    v2=[cnt[1][0][0]-cnt[2][0][0],cnt[1][0][1]-cnt[2][0][1]]
    v3=[cnt[2][0][0]-cnt[3][0][0],cnt[2][0][1]-cnt[3][0][1]]
    v4=[cnt[3][0][0]-cnt[0][0][0],cnt[3][0][1]-cnt[0][0][1]]
    eq1=isEqual(v1,v3)
    eq2=isEqual(v2,v4)
    eq3=isEqual(v1,v2)
    #print(v1,v2,v3,v4)
    #print(isParallel(v1,v3), isParallel(v2,v4))
    #checking for shapes having al least opposite sides equal
    if(eq1 and eq2) :
        obj="Parallelogram"
        #print(cnt)
        if(isPerpendicular(v1,v2)):
            
            obj="Rectangle"
        if(eq3):
            obj="Rhombus"
            if(isPerpendicular(v1,v2)):
                obj="Square"
    if(obj=="Quadrilateral"):
        #none of the above cases were true then check for trapezium
        if(isParallel(v1,v3) or isParallel(v2,v4)):
            obj="Trapezium"
    #print(obj)
    return obj
    
def isEqual(v1,v2):
    ratio=(v1[0]**2+v1[1]**2)/(v2[0]**2+v2[1]**2)
    #print("Equal ratio=",ratio)
    if ratio > 0.97 and ratio < 1.03:
        return True
    else:
        return False
def isPerpendicular(v1,v2):
    #print(v1,v2)
    #v2=complex(v2[0],v2[1])
    #v1=complex(v1[0],v1[0])
    #print(v1,v2)
    #angle=abs(np.angle(v2/v1,deg=True))
    #print("Perpendicular angle=",angle)
    #if(angle>85 and angle<95)or(angle<-85 and angle>-95) :
        #return True
    #checking for prouct of slopes
    #pro=((v2[1]/v2[0])*(v1[1]/v1[0]))
    #print("Perprndicular Product:",pro)
    #if pro<=-0.97 and pro >=-1.03:
        #return True
    #else:
        #return False
    #doing dot product of vectors
    dot=(v1[0]*v2[0]+v2[1]*v1[1])/((v1[0]**2+v1[1]**2)**(0.5)*(v2[0]**2+v2[1]**2)**(0.5))
    #print(dot)
    if dot < 0.03 and dot > -0.03:
        return True
    else:
        return False
def isParallel(v1,v2):
    ratio=(v2[1]/v2[0])/(v1[1]/v1[0])
    #print("Parallel ratio=",ratio)
    if ratio > 0.97 and ratio < 1.03:
        return True
    else:
        return False


# In[58]:


##############################################################


def scan_image(img_file_path):

    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes

    ##############	ADD YOUR CODE HERE	##############
    shapes={}
    img = cv2.imread(img_file_path)
    #cv2.imshow("window",img)
    #plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret,thresh = cv2.threshold(imgGray,120,255,cv2.THRESH_BINARY)
    #plt.imshow(cv2.cvtColor(imgGray,cv2.COLOR_BGR2RGB))
    shapes=getContours(thresh,img)
    #print("Before Sort:",shapes)
    #sort the shapes according to area
    #kv is the tupple of ('Shape' , ('color', Area, cX, cY)), area is kv[1][1]
    shapes=dict(sorted(shapes.items(),key=lambda kv: kv[1][1]))
    
    #print(shapes)
    
    ##################################################
    
    return shapes
#path=os.getcwd()+"/Samples/Sample3.png";
#print(path)
#shapes = scan_image(path);


# In[59]:


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in '+ curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')
    
    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()
    
    print('\n============================================')

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')
        
        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2
        
        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')
            
            else:
                print('\n[ERROR] Sample' + str(file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()
            
            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')
                
                else:
                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')

