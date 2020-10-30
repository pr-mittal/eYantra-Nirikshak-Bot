#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1A - Part 2 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Author List:		Priyank Sisodia,Pranav Mittal
# Filename:			task_1a_part2.py
# Functions:		process_video
# 					[ Comma separated list of functions in this file ]
# Global variables:	frame_details
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


# In[3]:



# Global variable for details of frames seleced in the video will be put in this dictionary, returned from process_video function
frame_details = {}


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def process_video(vid_file_path, frame_list):

    """
    Purpose:
    ---
    this function takes file path of a video and list of frame numbers as arguments
    and returns dictionary containing details of red color circle co-ordinates in the frame

    Input Arguments:
    ---
    `vid_file_path` :		[ str ]
        file path of video
        `frame_list` :			[ list ]
        list of frame numbers

    Returns:
    ---
    `frame_details` :		[ dictionary ]
        co-ordinate details of red colored circle present in selected frame(s) of video
        { frame_number : [cX, cY] }

    Example call:
    ---
    frame_details = process_video(vid_file_path, frame_list)
    """

    global frame_details

    ##############	ADD YOUR CODE HERE	##############
    #capture video
    cap = cv2.VideoCapture(vid_file_path)
    #cap.set(3,500)    ##setting for width(3) 
    #cap.set(4,500)    ##setting for height(4) 
    #cap.set(10,100)   ##setting for brightness
    l1 = np.array([0,50,50])
    u1 = np.array([10,255,255])
    l2 = np.array([170,50,50])
    u2 = np.array([180,255,255])
    kernel = np.ones((5,5),np.uint8)
    frame_list= set(frame_list)
    #if (cap.isOpened()== False):
        #print("Error opening video stream or file")
    frame_n =0
    while (cap.isOpened()):
        # Capture frame-by-frame
        # ret = if the frame is collected or not (boolean),frame = part of video as a frame
        ret, img = cap.read()
        frame_n = frame_n +1
        #img =cv2.resize(img,(960,540))
        # Display the resulting frame
        #cv2.imshow('Frame', frame)
        if frame_n in frame_list:
            
            #imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
            imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            #cretaing mask
            m1 = cv2.inRange(imgHsv,l1,u1)
            m2 = cv2.inRange(imgHsv,l2,u2)
            m3 = m1+m2
            m3 = cv2.erode(m3,kernel,iterations =6)
            #m3=cv2.morphologyEx(m3, cv2.MORPH_OPEN, kernel,iterations=3)
            #plt.imshow(cv2.cvtColor(m3,cv2.COLOR_BGR2RGB))
            m3 = cv2.dilate(m3,kernel,iterations = 6)
            #plt.imshow(m3)
            output = cv2.bitwise_and(imgHsv, imgHsv, mask = m3)
            #working with a single contour
            contours, heirarchy = cv2.findContours(m3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            #print(len(contours)) only one contour is there
            if(len(contours)==1):
                maxcnt=contours[0]
            else:
                maxA=0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if(maxA<area):
                        maxA=area
                        maxcnt=cnt
            M = cv2.moments(maxcnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            #adding details to frame_details
            frame_details[frame_n]=[cX,cY]

        #print(f"/",frame_n,"--",cX*2,",",cY*2)
        #cv2.imshow('Frame', m3)
        if(ret==False):
            break
        
      # Press Q on keyboard to  exit
        #if cv2.waitKey(25) & 0xFF == ord('q'):
            #break
     # When everything done, release the video capture object(inportant)
    cap.release()
     # Closes all the frames
    #cv2.destroyAllWindows()
    #print(frame_list)
    ##################################################
    return frame_details
#process_video("/home/captain/projects/eYantra/Task1/task_1a_explore_opencv/Task_1A_Part2/Videos/ballmotion.m4v", [33,44,55])


# In[4]:



# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes input for selecting one of two videos available in Videos folder
#                   and a input list of frame numbers for which the details are to be calculated. It runs process_video
#                   function on these two inputs as argument.

if __name__ == '__main__':

	curr_dir_path = os.getcwd()
	print('Currently working in '+ curr_dir_path)

	# path directory of videos in 'Videos' folder
	vid_dir_path = curr_dir_path + '/Videos/'
	
	try:
		file_count = len(os.listdir(vid_dir_path))
	
	except Exception:
		print('\n[ERROR] "Videos" folder is not found in current directory.')
		exit()
	
	print('\n============================================')
	print('\nSelect the video to process from the options given below:')
	print('\nFor processing ballmotion.m4v from Videos folder, enter \t=> 1')
	print('\nFor processing ballmotionwhite.m4v from Videos folder, enter \t=> 2')
	
	choice = input('\n==> "1" or "2": ')

	if choice == '1':
		vid_name = 'ballmotion.m4v'
		vid_file_path = vid_dir_path + vid_name
		print('\n\tSelected video is: ballmotion.m4v')
	
	elif choice=='2':
		vid_name = 'ballmotionwhite.m4v'
		vid_file_path = vid_dir_path + vid_name
		print('\n\tSelected video is: ballmotionwhite.m4v')
	
	else:
		print('\n[ERROR] You did not select from available options!')
		exit()
	
	print('\n============================================')

	if os.path.exists(vid_file_path):
		print('\nFound ' + vid_name)
	
	else:
		print('\n[ERROR] ' + vid_name + ' file is not found. Make sure "Videos" folders has the selected file.')
		exit()
	
	print('\n============================================')

	print('\nEnter list of frame(s) you want to process, (between 1 and 404) (without space & separated by comma) (for example: 33,44,95)')

	frame_list = input('\nEnter list ==> ')
	frame_list = list(frame_list.split(','))

	try:
		for i in range(len(frame_list)):
			frame_list[i] = int(frame_list[i])
		print('\n\tSelected frame(s) is/are: ', frame_list)
	
	except Exception:
		print('\n[ERROR] Enter list of frame(s) correctly')
		exit()
	
	print('\n============================================')

	try:
		print('\nRunning process_video function on', vid_name, 'for frame following frame(s):', frame_list)
		frame_details = process_video(vid_file_path, frame_list)

		if type(frame_details) is dict:
			print(frame_details)
			print('\nOutput generated. Please verify')
		
		else:
			print('\n[ERROR] process_video function returned a ' + str(type(frame_details)) + ' instead of a dictionary.\n')
			exit()
	
	except Exception:
		print('\n[ERROR] process_video function is throwing an error. Please debug process_video function')
		exit()

	print('\n============================================')

