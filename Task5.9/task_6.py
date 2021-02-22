

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

# Team ID:          2182
# Author List:      Yatharth Bhargava,Priyank Sisodia,Aman Kumar,Pranav Mittal
# Filename:         task_5.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
#                   send_color_and_collection_box_identified,calculateMazeArrays,send_mazeData,getBallInfo,setup_maze_for_ball
#                   ,vs_conveyer,stopStreaming,stopSimulation,delete_path,read_ball_details,processMaze,main
# Global variables: 
# 					[ List of global variables defined in this file ]
#                   maze_all,vs_handle,totB,totM,client_id,ball_details


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
from threading import Thread
#import matplotlib.pyplot as plt
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
    
# Import 'task_4b.py' file as module
try:
    import task_4b

except ImportError:
    print('\n[ERROR] task_4b.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_4b.py is present in this current directory.\n')


except Exception as e:
    print('Your task_4b.py throwed an Exception. Kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)

##############################################################


# In[2]:



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

    color_and_cb = [ball_color + '::' + collection_box_name]
    inputBuffer = bytearray()
    return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id,'evaluation_screen_respondable_1',
                            sim.sim_scripttype_childscript,'color_and_cb_identification',[],[],color_and_cb,inputBuffer,sim.simx_opmode_blocking)


# In[3]:


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
maze_all=[-1,-1,-1,-1,-1]#we use maze_all starting from 1
vs_handle=[-1,-1,-1,-1,-1,-1]##we use vs_handle starting from 1
totB=3#check , total number of balls expected
totM=[1,2,3,4]#check , list of all maze numbers
client_id=-1
ball_details={}
processX=[]
############################################################################


# In[5]:


def calculateMazeArrays():
    global totM,maze_all
    # path directory of images in 'test_cases' folder
    #img_dir_path = 'test_cases/'
    img_dir_path=""
    for file_num in totM:
        # path to 'mazet4.jpeg' image file
        img_file_path = img_dir_path + 'maze_t' + str(file_num) + '.jpg'

        print('\n============================================')
        print('\nFor maze_t' + str(file_num) + '.jpeg')

        if os.path.exists(img_file_path):    

            try:
                # read the 'maze00.jpg' image file
                input_img = cv2.imread(img_file_path)
                #plt.imshow(cv2.cvtColor(input_img,cv2.COLOR_BGR2RGB))
                if type(input_img) is np.ndarray:

                    try:
                        # get the resultant warped maze image after applying Perspective Transform
                        warped_img = task_1b.applyPerspectiveTransform(input_img)
                        #plt.imshow(cv2.cvtColor(warped_img,cv2.COLOR_BGR2RGB))
                        if type(warped_img) is np.ndarray:

                            try:
                                # get the encoded maze in the form of a 2D array
                                maze_all[file_num] = task_1b.detectMaze(warped_img)
                                #plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
                                print(maze_all[file_num])
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
            print('\n[ERROR] mazet' + str(file_num) + '.jpeg not found.')
            print('Your current directory is: ', os.getcwd())
###################################################################################################################


# In[7]:


def send_mazeData():
    global totM,maze_all,client_id
    try:
        # Send maze array data to CoppeliaSim via Remote API
        for table_number in totM:
            print("Sending Maze to table_number "+str(table_number))
            #print(maze_all[table_number])
            
            return_code = task_2b.send_data(client_id,maze_all[table_number],table_number)
            if(return_code!=sim.simx_return_ok):
                #try resending the data
                print('\n[ERROR] Failed sending data to CoppeliaSim!')
                print('send_data function in task_2b.py is not configured correctly, check the code!')
                #return_code = task_2b.send_data(client_id,maze_array,table_number)
                #print()
                #sys.exit()
            else:
                print("Successfully sent maze data to ",table_number)
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


# In[6]:


#########################################################################################################
#get all info of journey of ball
def getBallInfo(ball_color):
    global ball_details,maze_all,vs_handle
    ball_info=[4,[],-1,[]]
    #current table number,path in table 4,[path,vision_sensor_handle,revolute_handle],table x,[path in x,vision_sensor_handle,revolute_handle]
    #ball_color ="blue"
    #cb = "T4_CB1"
    #print(ball_details)
    try:
        collection_box_name=ball_details[ball_color][0]
    except Exception:
        print('\n[ERROR] Your getBallInfo function in task_5.py throwed an Exception. Kindly debug your code!')
        print("Check Balll details ",ball_details," for colour ",ball_color)
        return None
        # traceback.print_exc(file=sys.stdout)
        # print()
        # sys.exit()
    #removing this from ball_details
    if(len(ball_details[ball_color])==1):
        #remove color from ball
        ball_details.pop(ball_color)
    else:
        #remove that collection box from list
        ball_details[ball_color].pop(0)
    print("Ball details New: ",ball_details)

    table = int(collection_box_name[1])
    box =int(collection_box_name[-1])
    print("Finding path to "+collection_box_name+" via table "+str(table)+" to box "+str(box))
    #starting cordinates and ending cordinates for path in table 4
    start_coord = (0,5)
    if(table==1):
        end_coord = (5,9)
        out_coord=(5,9.6)
    if(table==2):
        end_coord = (9,4)
        out_coord=(9.6,4)
    if(table==3):
        end_coord = (4,0)
        out_coord=(4,-0.6)
                
    #from table 4 to exit and storing in ball_info at index1
    #print(maze_all[4],start_coord, end_coord)
    ball_info[1] = task_4a.find_path(maze_all[4],start_coord, end_coord)
    ball_info[1].append(out_coord)
    
    print("Path in table 4:"+str(ball_info[1]))

    if(table==1):
        start_coord = (5,0)
        if(box==1):
            end_coord = (0,4)
            out_coord=(-0.6,4)
        if(box==2):
            end_coord = (4,9)
            out_coord=(4,9.6)
        if(box==3):
            end_coord = (9,5)
            out_coord=(9.6,5)
    if(table==2):
        start_coord = (0,4)
        if(box==1):
            end_coord = (4,9)
            out_coord=(4,9.6)
        if(box==2):
            end_coord = (9,5)
            out_coord=(9.6,5)
        if(box==3):
            end_coord = (5,0)
            out_coord=(5,-0.6)
    if(table==3):
        start_coord = (4,9)
        if(box==1):
            end_coord = (9,5)
            out_coord=(9.6,5)
        if(box==2):
            end_coord = (5,0)
            out_coord=(5,-0.6)
        if(box==3):
            end_coord = (0,4)
            out_coord=(-0.6,4)
    ball_info[2]=table
    #from table 4 to exit and storing in ball_info at index1
    #print(maze_all[table],start_coord, end_coord)
    ball_info[3] = task_4a.find_path(maze_all[table],start_coord, end_coord)
    ball_info[3].append(out_coord)
    print("Path in table "+str(table)+":"+str(ball_info[3]))
    
    #calling for grading app
    #send_color_and_collection_box_identified(ball_color, collection_box_name)
    return ball_info
##############################################################


# In[ ]:


def setup_maze_for_ball(client_id,table_number,path):
    #start checking for ball on table_number
    path_handle=-1
    #if found start pid
    try:
        revolute_handle,vision_sensor_handle=task_3.init_setup(client_id,table_number)
        try:
            path_handle=task_4b.send_data_to_draw_path(client_id, path,table_number)
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
    return revolute_handle,vision_sensor_handle,path_handle
#########################################################################################################


# In[4]:


def setup_scene():
    global client_id,vs_handle,totM
    for table_number in totM:
        
        _,vs_handle[table_number]=sim.simxGetObjectHandle(client_id, 'vision_sensor_'+str(table_number), sim.simx_opmode_blocking)
        _, _, _ = sim.simxGetVisionSensorImage(client_id,vs_handle[table_number], 0, sim.simx_opmode_discontinue)

    _, vs_handle[5] = sim.simxGetObjectHandle(client_id, 'vision_sensor_5', sim.simx_opmode_blocking)
    _, _, _ = sim.simxGetVisionSensorImage(client_id,vs_handle[5], 0, sim.simx_opmode_streaming)
    _,_= sim.simxGetPingTime(client_id)
    
    for table_number in totM:
        #set all model non renderable
        return_code,object_handle=sim.simxGetObjectHandle(client_id,"base_plate_respondable_t"+str(table_number)+"_1",sim.simx_opmode_blocking)
        if(table_number!=4):
            return_code = sim.simxSetModelProperty(client_id,object_handle,1135,sim.simx_opmode_blocking)
        else:
            return_code = sim.simxSetModelProperty(client_id,object_handle,0,sim.simx_opmode_blocking)
####################################################################################################
def stopStreaming(vision_sensor_handle):
    #vision_sensor_handle=vs_handle[vs_number]
    _, _, _ = sim.simxGetVisionSensorImage(client_id,vision_sensor_handle, 0, sim.simx_opmode_discontinue)
    _,_= sim.simxGetPingTime(client_id)
#######################################################################################################


# In[8]:


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


# In[9]:


def delete_path(rec_client_id,table_number,handle):
    #global client_id
    client_id = rec_client_id
    inputBuffer = bytearray()
    return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id, 'top_plate_respondable_t'+str(table_number)+'_1', sim.sim_scripttype_customizationscript, 'deletePath', [handle],[], [], inputBuffer, sim.simx_opmode_blocking)
    if(return_code!=sim.simx_return_ok):
        print('\n[ERROR] Your delete_path() function throwed an Exception. Kindly debug your code!')
        #print('Stop the CoppeliaSim simulation manually.\n')
        #traceback.print_exc(file=sys.stdout)
        #print()
        #sys.exit()
        return 0
    return retInts[0]
##################################################


# In[11]:


###################################################################################################
def read_ball_details(file_name):
    global ball_details
    f=open(file_name,)
    ball_details=json.load(f)
    print("Ball Details:",ball_details)
##############################################################################################
def processMaze(client_id,ball_info,revolute_handle,vision_sensor_handle,path_handle):
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
        
    # Import 'task_4b.py' file as module
    try:
        import task_4b

    except ImportError:
        print('\n[ERROR] task_4b.py file is not present in the current directory.')
        print('Your current directory is: ', os.getcwd())
        print('Make sure task_4b.py is present in this current directory.\n')


    except Exception as e:
        print('Your task_4b.py throwed an Exception. Kindly debug your code!\n')
        traceback.print_exc(file=sys.stdout)

    #print(vision_sensor_handle,client_id)
    try:
        #print(client_id,ball_info,revolute_handle,vision_sensor_handle)
        #if this table is current table in dictionary of ball
        #check if ball in vision sensor table 4
        print("Checking for ball in table "+str(ball_info[0]),end="")
        while(True):
            #process 1
            #check if ball in stream of vision sensor conveyer
            # print(" . ",end="")
            # print(client_id,vision_sensor_handle)
            shapes=task_4b.getBallData(client_id,vision_sensor_handle,True)
            # print(shapes)
            if(shapes==None):
                continue
            if(len(shapes)!=0):
            #if ball detected , start pid
                print("\nBall detected in table "+str(ball_info[0]),"  shapes:",shapes)
                try:
                    pixel_path = task_4b.convert_path_to_pixels(ball_info[1])
                    #print('\nPath calculated between %s and %s in pixels is = %s' % (start_coord, end_coord, pixel_path))
                    #print('\n============================================')
                    print("Started traversing table :"+str(ball_info[0]))
                    try:
                        time.sleep(15)
                        # task_4b.traverse_path(client_id,pixel_path,vision_sensor_handle,revolute_handle,ball_info[0])
                    except Exception:
                        print('\n[ERROR] Your traverse_path() function throwed an Exception. Kindly debug your code!')
                        #print('Stop the CoppeliaSim simulation manually.\n')
                        #traceback.print_exc(file=sys.stdout)
                        #print()
                        #sys.exit()

                except Exception:
                    print('\n[ERROR] Your convert_path_to_pixels() function throwed an Exception. Kindly debug your code!')
                    print('Stop the CoppeliaSim simulation manually.\n')
                    #traceback.print_exc(file=sys.stdout)
                    #print()
                    #sys.exit()
                    
                #delete Path
                print("Deleteing Path in table "+str(ball_info[0]))
                delete_path(client_id,ball_info[0],path_handle)
                #make table non respondable , non collidable etc.
                
                #if this is not table 4 return, journey of ball is complete
                if(ball_info[0]!=4):
                    return
                #start vision sensor for next ball from this table
                #print(client_id,ball_info[2],ball_info[3])
                revolute_handle,vision_sensor_handle,path_handle=setup_maze_for_ball(client_id,ball_info[2],ball_info[3])
                #make the next table renderable
                invert_model_properties(client_id,ball_info[2])

                #process 3
                #change currrent table in list ball_info
                ball_info[0]=ball_info[2]
                #changing current path
                ball_info[1]=ball_info[3]

                #start checking for ball in next table
                #do same thing as in process 2
                print("Starting setup for ball in table "+str(ball_info[0]))
                processMaze(client_id,ball_info,revolute_handle,vision_sensor_handle,path_handle)
                print("Sent ball to collection box in table "+str(ball_info[0]))
                #stop streaming this vision sensor
                stopStreaming(vision_sensor_handle)
                #make this table non renderable
                invert_model_properties(client_id,ball_info[0])
                break
    except Exception:
        print('\n[ERROR] Your processMaze function in task_5.py throwed an Exception. Kindly debug your code!')
        print('Stop the CoppeliaSim simulation manually.\n')
        traceback.print_exc(file=sys.stdout)
        print()
        sys.exit()


# In[10]:
def invert_model_properties(client_id,table_number):
    # NOTE: This function will be used to invert model properties such that the model which is not to be
    # 		traversed in the current iteration can be partially disabled thereby saving the computational
    #		resources.
    return_code,object_handle=sim.simxGetObjectHandle(client_id,"base_plate_respondable_t"+str(table_number)+"_1",sim.simx_opmode_blocking)
    return_code, curr_model_prop = sim.simxGetModelProperty(client_id,object_handle,sim.simx_opmode_blocking)
    #print(curr_model_prop)
    if(curr_model_prop == 0):
        # Overrides the required model props as NOT measureable, NOT dynamic, NOT collidable, NOT
        # renderable, NOT detectable, NOT respondable and Invisible to other model's bounding boxes.
        return_code = sim.simxSetModelProperty(client_id,object_handle,1135,sim.simx_opmode_blocking)
        print("Non renderable table ",table_number)
    else:
        return_code = sim.simxSetModelProperty(client_id,object_handle,0,sim.simx_opmode_blocking)
        print("Renderable table ",table_number)
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
    global maze_all,vs_handle,client_id,ball,totB,totM,processX
    client_id=rec_client_id

    if (client_id != -1):
        print('\nConnected successfully to Remote API Server in CoppeliaSim!')
    else:
        print('\n[ERROR] Your init_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
        return
    
    #global variables
    #maze arrays,vision sensor handles,dictionary about ball,number of balls passed,totalballs
    
    #make maze arrays, store maze arrays
    print("Calcute Maze Arrays")
    calculateMazeArrays()
    #print(maze_all)
    #send maze arrays to coppeliasim and start simulation
    print("Sending Data to Maze in Scene")
    send_mazeData()
    #start vision streaming vision sensor conveyer and check for ball,store all vision sensor handles
    print("Started Streaming vision sensor conveyer and disable collision")
    setup_scene()
    print("Vision Sensor handles ",vs_handle)
    #read json file for ball details
    read_ball_details("ball_details.json")
    
    ############check maze,will be seen at last################################
    curB=0
    count_time=0#counts time after a ball was spotted
    #keeps track of time when new ball is spotted in vision sensor conveyer
    return_code,prev_time=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)
    if(return_code == 0):
        prev_time=float(prev_time)
    else:
        prev_time=0.0
    threshCount=20#ball missing from vision sensor for this time, means we can start waiting for next ball
    
    print("Waiting for ball in vision sensor conveyer",end="")
    #while true
    while(True):
        #process 1
        #check if ball in stream of vision sensor conveyer
        # print(" . ",end="")
        # shapes=task_4b.getBallData(client_id,vs_handle[5],False)        
        
        #check is this is a new ball
        return_code,now=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
        if(return_code== 0):
            try:
                now=float(now)
            except Exception:
                continue
            #print("Now=",now)
        else:
            continue

        count_time=float(now)-prev_time
        if((count_time<threshCount) and (curB!=0)):
            continue
        

        vision_sensor_image, image_resolution, return_code = task_2a.get_vision_sensor_image(client_id,vs_handle[5])
        if ((return_code != sim.simx_return_ok) or (len(image_resolution) != 2) or (len(vision_sensor_image) <= 0)):
            #print('\n[ERROR] Your get_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
            #print('Stop the CoppeliaSim simulation manually.\n')
            #traceback.print_exc(file=sys.stdout)
            #print()
            #sys.exit()
            continue
        # Get the transformed vision sensor image captured in correct format
        try:
            transformed_image = task_2a.transform_vision_sensor_image(vision_sensor_image, image_resolution)
            if (type(transformed_image) is np.ndarray):
                warped_img = transformed_image
                warped_img = cv2.resize(warped_img, (1280, 1280))
                try:
                    shapes = task_1a_part1.scan_image(warped_img)
                    if (type(shapes) is dict and shapes!={}):
                        #print(shapes)
                        if( type(shapes['Circle'][0]) is list ):
                            continue
                        #print("Found")
                    elif(type(shapes) is not dict):
                        continue
                except Exception:
                    print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception. Kindly debug your code!')
                    #print('Stop the CoppeliaSim simulation manually.\n')
                    #traceback.print_exc(file=sys.stdout)
                    #print()
                    #sys.exit()
            else:
                print('\n[ERROR] transform_vision_sensor_image function in task_2a.py is not configured correctly, check the code.')
                #print('Stop the CoppeliaSim simulation manually.')
                #print()
                #sys.exit()

        except Exception:
            print('\n[ERROR] Your transform_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
            #print('Stop the CoppeliaSim simulation manually.\n')
            #traceback.print_exc(file=sys.stdout)
            #print()
            #sys.exit()
        # print(shapes)
        if(len(shapes)!=0):
            #if ball found,add 1 to number of ball
            # print(shapes)
            curB+=1
            count_time=0
            return_code,prev_time=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
            if(return_code== 0):
                prev_time=float(prev_time)
                #print("Now=",now)

            color=shapes['Circle'][0]
            print("\nFound "+color+" ball in vision coveyer")
            #get info of ball from ball_details [current table number,path in table 4,table x,path in table x]
            #differentiate balls based on color
            ball_info=getBallInfo(color)
            if(ball_info==None):
                continue
            #start streaming of table 4 vision sensor
            print("setup maze 4 for ball to come")
            revolute_handle,vision_sensor_handle,path_handle=setup_maze_for_ball(client_id,4,ball_info[1])

            #start task3 in multiprocessing
            #with concurrent.futures.ProcessPoolExecutor() as executor:
            #    f1=executor.submit(processMaze(table_number),1)
            print("Started a subprocess for this ball")
            #processMaze(client_id,ball_info,revolute_handle,vision_sensor_handle,path_handle)
            # print(client_id,revolute_handle,vision_sensor_handle)
            # process=Process(target=processMaze,args=(client_id,ball_info,revolute_handle,vision_sensor_handle,path_handle,))
            process=Thread(target=processMaze,args=(client_id,ball_info,revolute_handle,vision_sensor_handle,path_handle,))
            
            #processes are spawned by creating Process object and calling its start method
            process.start()
            #process.join()
            #process.join()
            processX.append(process)
            #if this is last ball stop streaming vision conveyer
            #print(curB,totB,curB==totB)
            if(curB==totB):
                print("Max balls for this has passed , stopping vision sensor conveyer stream.")
                stopStreaming(vs_handle[5])
                break
    for process in processX:
       process.join()

    #end simulation
    time.sleep(3)
    # stopSimulation(client_id)
    ##################################################


# In[12]:


#Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    To call the main(rec_client_id) function written by teams when they
#					run task_5.py only.

# NOTE: Write your solution ONLY in the space provided in the above functions. This function should not be edited.
if __name__ == "__main__":

    client_id = task_2a.init_remote_api_server()
    main(client_id)

