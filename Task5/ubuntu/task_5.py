#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 5 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD (now MOE) project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          [ Team-ID ]
# Author List:      [ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         task_5.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]

# NOTE: Make sure you do NOT call sys.exit() in this code.

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
##############################################################
import numpy as np
import cv2
import os, sys
import traceback
import time
import math
import json
###############################################################
from multiprocessing import Process
#import concurrent.futures
##############################################################

# Importing the sim module for Remote API connection with CoppeliaSim
try:
    import sim

except Exception:
    print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
    print('\n[WARNING] Make sure to have following files in the directory:')
    print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')


#Import 'task_1b.py' file as module
try:
    import task_1b

except ImportError:
    print('\n[ERROR] task_1b.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_1b.py is present in this current directory.\n')


except Exception as e:
    print('Your task_1b.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)



# Import 'task_1a_part1.py' file as module
try:
    import task_1a_part1

except ImportError:
    print('\n[ERROR] task_1a_part1.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_1a_part1.py is present in this current directory.\n')


except Exception as e:
    print('Your task_1a_part1.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)



# Import 'task_2a.py' file as module
try:
    import task_2a

except ImportError:
    print('\n[ERROR] task_2a.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_2a.py is present in this current directory.\n')


except Exception as e:
    print('Your task_2a.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)


# Import 'task_2b.py' file as module
try:
    import task_2b

except ImportError:
    print('\n[ERROR] task_2b.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_2b.py is present in this current directory.\n')


except Exception as e:
    print('Your task_2b.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)


# Import 'task_3.py' file as module
try:
    import task_3

except ImportError:
    print('\n[ERROR] task_3.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_3.py is present in this current directory.\n')


except Exception as e:
    print('Your task_3.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)



# Import 'task_4a.py' file as module
try:
    import task_4a

except ImportError:
    print('\n[ERROR] task_4a.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_4a.py is present in this current directory.\n')


except Exception as e:
    print('Your task_4a.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)

##############################################################


# In[ ]:



# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    send_color_and_collection_box_identified
#        Inputs:    ball_color and collection_box_name
#       Outputs:    None
#       Purpose:    1. This function should only be called when the task is being evaluated using
# 					   test executable.
#					2. The format to send the data is as follows:
#					   'color::collection_box_name'				   
def send_color_and_collection_box_identified(ball_color, collection_box_name):

    global client_id

    color_and_cb = ball_color + '::' + collection_box_name
    inputBuffer = bytearray()
    return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id,'evaluation_screen_respondable_1',
                            sim.sim_scripttype_childscript,'color_and_cb_identification',[],[],color_and_cb,inputBuffer,sim.simx_opmode_blocking)


# In[ ]:


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
maze_all=[[],[],[],[],[]]#we use maze_all starting from 1
vs_handle=[[],[],[],[],[],[]]##we use vs_handle starting from 1
curB=0
totB=1
totM=[1,4]
client_id=-1
ball_details={}
process=[]
############################################################################


# In[ ]:


def calculateMazeArrays():
    global totM,maze_all
    # path directory of images in 'test_cases' folder
    img_dir_path = 'test_cases/'
    for file_num in totM:
        # path to 'mazet4.jpeg' image file
        img_file_path = img_dir_path + 'mazet' + str(file_num) + '.jpeg'

        print('\n============================================')
        print('\nFor mazet' + str(file_num) + '.jpeg')

        if os.path.exists(img_file_path):

            try:
                # read the 'maze00.jpg' image file
                input_img = cv2.imread(img_file_path)

                if type(input_img) is np.ndarray:

                    try:
                        # get the resultant warped maze image after applying Perspective Transform
                        warped_img = task_1b.applyPerspectiveTransform(input_img)

                        if type(warped_img) is np.ndarray:

                            try:
                                # get the encoded maze in the form of a 2D array
                                maze_array[file_num] = task_1b.detectMaze(warped_img)
                            except Exception:
                                print('\n[ERROR] Your detectMaze function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
                                #traceback.print_exc(file=sys.stdout)
                                #print()
                                #sys.exit()
                        else:
                            print('\n[ERROR] applyPerspectiveTransform function in \'task_1b.py\' is not returning the warped maze image in expected format!, check the code.')
                            #print()
                            #sys.exit()
                    except Exception:
                        print('\n[ERROR] Your applyPerspectiveTransform function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
                        #traceback.print_exc(file=sys.stdout)
                        #print()
                        #sys.exit()

                else:
                    print('\n[ERROR] maze0' + str(file_num) + '.jpg was not read correctly, something went wrong!')
                    #print()
                    #sys.exit()

            except Exception:
                print('\n[ERROR] Your calculate_path_from_maze_image() function throwed an Exception. Kindly debug your code!')
                print('Stop the CoppeliaSim simulation manually.\n')
        else:
            print('\n[ERROR] mazet' + str(file_num) + '.jpeg not found. Make sure "test_cases" folder is present in current directory.')
            print('Your current directory is: ', os.getcwd())
###################################################################################################################


# In[ ]:


def send_mazeData():
    global totM,maze_all,client_id
    try:
        # Send maze array data to CoppeliaSim via Remote API
        for table_number in totM:
            return_code = task_2b.send_data(client_id,maze_array,table_number)
            if(return_code!=sim.simx_return_ok):
                #try resending the data
                print('\n[ERROR] Failed sending data to CoppeliaSim!')
                print('send_data function in task_2b.py is not configured correctly, check the code!')
                #return_code = task_2b.send_data(client_id,maze_array,table_number)
                #print()
                #sys.exit()

    except Exception:
        print('\n[ERROR] Your send_data function throwed an Exception, kindly debug your code!')
        #traceback.print_exc(file=sys.stdout)
        #print()
        #sys.exit()
        
    # Starting the Simulation
    try:
        return_code = task_2a.start_simulation(client_id)        
        if (return_code == sim.simx_return_novalue_flag):
            print('\nSimulation started correctly in CoppeliaSim.')
        else:
            print('\n[ERROR] Failed starting the simulation in CoppeliaSim!')
            print('start_simulation function in task_2a.py is not configured correctly, check the code!')
            #print()
            #sys.exit()

    except Exception:
        print('\n[ERROR] Your start_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
        #print('Stop the CoppeliaSim simulation manually.\n')
        #traceback.print_exc(file=sys.stdout)
        #print()
        #sys.exit()
#################################################################################################


# In[ ]:


def vs_conveyer():
    global client_id,vs_handle,totM
    for table_number in totM:
        _,vs_handle[table_number]=sim.simxGetObjectHandle(client_id, 'vision_sensor_'+table_number, sim.simx_opmode_blocking)
    _, vs_handle[5] = sim.simxGetObjectHandle(client_id, 'vision_sensor_5', sim.simx_opmode_blocking)
    _, _, _ = sim.simxGetVisionSensorImage(client_id,vs_handle[5], 0, sim.simx_opmode_streaming)
    rCode,pingTime= sim.simxGetPingTime(client_id)
####################################################################################################
def stopStreaming(vs_number):
    vision_sensor_handle=vs_handle[vs_number]
    _, _, _ = sim.simxGetVisionSensorImage(client_id,vision_sensor_handle, 0, sim.simx_opmode_discontinue)
    rCode,pingTime= sim.simxGetPingTime(client_id)
#######################################################################################################


# In[ ]:


def setup_maze_for_ball(client_id,table_number,path):
    #start checking for ball on table_number
    
    #if found start pid
    try:
        revolute_handle,vision_sensor_handle=task_3.init_setup(client_id,table_number)
        try:
            send_data_to_draw_path(client_id,path)
        except Exception:
            print('\n[ERROR] Your send_data_to_draw_path() function throwed an Exception. Kindly debug your code!')
            #print('Stop the CoppeliaSim simulation manually.\n')
            #traceback.print_exc(file=sys.stdout)
            #print()
            #sys.exit()
    except Exception:
        print('\n[ERROR] Your init_setup() function throwed an Exception. Kindly debug your code!')
        #print('Stop the CoppeliaSim simulation manually if started.\n')
        #traceback.print_exc(file=sys.stdout)
        #print()
        #sys.exit()
    return revolute_handle,vision_sensor_handle
def stopSimulation(client_id):
    try:
        return_code = task_2a.stop_simulation(client_id)

        if (return_code == sim.simx_return_novalue_flag):
            print('\nSimulation stopped correctly.')

            # Stop the Remote API connection with CoppeliaSim server
            try:
                task_2a.exit_remote_api_server(client_id)
            except Exception:
                print('\n[ERROR] Your exit_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
                print('Stop the CoppeliaSim simulation manually.\n')
                #traceback.print_exc(file=sys.stdout)
                #print()
                #sys.exit()

        else:
            print('\n[ERROR] Failed stopping the simulation in CoppeliaSim server!')
            print('[ERROR] stop_simulation function in task_2a.py is not configured correctly, check the code!')
            print('Stop the CoppeliaSim simulation manually.')
            #print()
            #sys.exit()

    except Exception:
        print('\n[ERROR] Your stop_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
        print('Stop the CoppeliaSim simulation manually.\n')
        #traceback.print_exc(file=sys.stdout)
        #print()
        #sys.exit()


# In[ ]:


#get all info of journey of ball
def getBallInfo(ball_color):
    global ball_details,maze_all,vs_handle
    ball_info=[[4],[],[],[]]
    #current table number,path in table 4,[path,vision_sensor_handle,revolute_handle],table x,[path in x,vision_sensor_handle,revolute_handle]
    #ball_color ="blue"
    #cb = "T4_CB1"
    collection_box_name=ball_details[ball_color][0]
    #removing this from ball_details
    if(len(ball_details[ball_color])==1):
        #remove color from ball
        ball_details.pop(ball_color)
    else:
        #remove that collection box from list
        ball_details[ball_color].pop(0)
    table = int(collection_box_name[1])
    box =int(collection_box_name[-1])
    #starting cordinates and ending cordinates for path in table 4
    start_cordinates = [0,5]
    if(table==1):
        end_cordinates = [5,9]
    if(table==2):
        end_cordinates = [9,4]
    if(table==3):
        end_cordinates = [4,0]
                
    #from table 4 to exit and storing in ball_info at index1
    maze_array, ball_info[1] = task_4b.calculate_path_from_maze(maze_all[4],start_coord, end_coord)
    
    if(table==1):
        start_cordinates = [5,0]
        if(box==1):
            end_cordinates = [0,4]
        if(box==2):
            end_cordinates = [4,9]
        if(box==3):
            end_cordinates = [9,5]
    if(table==2):
        start_cordinates = [0,4]
        if(box==1):
            end_cordinates = [4,9]
        if(box==2):
            end_cordinates = [9,5]
        if(box==3):
            end_cordinates = [5,0]
    if(table==3):
        start_cordinates = [4,9]
        if(box==1):
            end_cordinates = [9,5]
        if(box==2):
            end_cordinates = [5,0]
        if(box==3):
            end_cordinates = [0,4]
    ball_info[2]=table
    #from table 4 to exit and storing in ball_info at index1
    maze_array, ball_info[3] = task_4b.calculate_path_from_maze(maze_all[table],start_coord, end_coord)
    return ball_info
##############################################################


# In[ ]:


###################################################################################################
def read_ball_details(file_name):
    global ball_details
    f=open(file_name,)
    ball_details=json.load(f)
##############################################################################################
def processMaze(client_id,ball_info,revolute_handle,vision_sensor_handle):
    #if this table is current table in dictionary of ball
    #check if ball in vision sensor table 4
    while(True):
        #process 1
        #check if ball in stream of vision sensor conveyer
        shapes=task4b.getBallData(client_id,vision_sensor_handle)
        if(len(shapes)!=0):
        #if ball detected , start pid
                try:
                    pixel_path = task4b.convert_path_to_pixels(ball_info[1])
                    print('\nPath calculated between %s and %s in pixels is = %s' % (start_coord, end_coord, pixel_path))
                    #print('\n============================================')

                    try:
                        task4b.traverse_path(client_id,pixel_path,vision_sensor_handle,revolute_handle)
                    except Exception:
                        print('\n[ERROR] Your traverse_path() function throwed an Exception. Kindly debug your code!')
                        print('Stop the CoppeliaSim simulation manually.\n')
                        #traceback.print_exc(file=sys.stdout)
                        #print()
                        #sys.exit()

                except Exception:
                    print('\n[ERROR] Your convert_path_to_pixels() function throwed an Exception. Kindly debug your code!')
                    print('Stop the CoppeliaSim simulation manually.\n')
                    #traceback.print_exc(file=sys.stdout)
                    #print()
                    #sys.exit()
            
            #if this is not table 4 return, journey of ball is complete
            if(ball_info[0]!=4):
                return
            
            #start vision sensor for next ball from this table
            #setup_maze_for_ball(client_id,table_number,path)
            revolute_handle,vision_sensor_handle=setup_maze_for_ball(client_id,ball_info[2],ball_info[3])
            #process 3
            #change currrent table in list ball_info
            ball_info[0]=ball_info[2]
            #changing current path
            ball_info[1]=ball_info[3]
            
            #start checking for ball in next table
            #do same thing as in process 2
            processMaze(client_id,ball_info,revolute_handle,vision_sensor_handle)
            ####################also delete current ball from dictionary######################not done yet
            #stop streaming this vision sensor
            stopStreaming(vision_sensor_handle)
                


# In[4]:


def main(rec_client_id):
    """
    Purpose:
    ---

    Teams are free to design their code in this task.
    The test executable will only call this function of task_5.py.
    init_remote_api_server() and exit_remote_api_server() functions are already defined
    in the executable and hence should not be called by the teams.
    The obtained client_id is passed to this function so that teams can use it in their code.

    However NOTE:
    Teams will have to call start_simulation() and stop_simulation() function on their own. 

    Input Arguments:
    ---
    `rec_client_id` 	:  integer
        client_id returned after calling init_remote_api_server() function from the executable.

    Returns:
    ---
    None

    Example call:
    ---
    main(rec_client_id)

    """
    ##############	ADD YOUR CODE HERE	##############
    global maze_all,vs_handle,client_id,ball,curB,totB,totM
    client_id=rec_client_id
    if (client_id != -1):
        print('\nConnected successfully to Remote API Server in CoppeliaSim!')
    else:
        print('\n[ERROR] Your init_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
        return
    
    #global variables
    #maze arrays,vision sensor handles,dictionary about ball,number of balls passed,totalballs
    
    #make maze arrays, store maze arrays
    calculateMazeArrays()
    #send maze arrays to coppeliasim and start simulation
    send_mazeData()    
    #start vision streaming vision sensor conveyer and check for ball,store all vision sensor handles
    vs_conveyer()
    #read json file for ball details
    read_ball_details("ball_details.json")
    
    #########################################check maze,will be seen at last
    newBall=True#che
    count=0
    threshCount=10#balling missing from vision sensor for this many frames, means we can start waiting for next ball
    #while true
    while(True):
        #process 1
        #check if ball in stream of vision sensor conveyer
        shapes=task4b.getBallCoordinates(vs_handle[5])
        if((len(shapes)!=0) and newBall):
            #if ball found,add 1 to number of ball
            curB+=1
            newBall=False
            #get info of ball from ball_details current table number,path in table 4,path in table x,table x
            #differentiate balls based on color
            ball_info=getBallInfo(color)
            
            #start streaming of table 4 vision sensor
            revolute_handle,vision_sensor_handle=setup_maze_for_ball(client_id,table_number,path)
            
            #start task3 in multiprocessing
            #with concurrent.futures.ProcessPoolExecutor() as executor:
            #    f1=executor.submit(processMaze(table_number),1)
            
            process=Process(target=processMaze,args=(client_id,ball_info,revolute_handle,vision_sensor_handle,))
            #processes are spawned by creating Process object and calling its start method
            process.start()
            
            #if this is last ball stop streaming vision conveyer
            if(curB==totB):
                stopStreaming(vs_handle[5])
                break
        else:
            count+=1
            if(count>threshCount):
                newBall=True
            
    ##################################################


# In[ ]:


Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    To call the main(rec_client_id) function written by teams when they
#					run task_5.py only.

# NOTE: Write your solution ONLY in the space provided in the above functions. This function should not be edited.
if __name__ == "__main__":

   client_id = task_2a.init_remote_api_server()
   main(client_id)

