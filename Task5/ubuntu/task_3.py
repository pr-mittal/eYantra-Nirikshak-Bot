'''
*****************************************************************************************
*
*				===============================================
*		   		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*				===============================================
*
*  This script is to implement Task 3 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:		NB_2182
# Author List:	  	Priyank Sisodia,Aman Sharma, Yatharth Bhargava, Pranav Mittal
# Filename:		 task_3.py
# Functions:		init_setup(rec_client_id), control_logic(center_x,center_y), change_setpoint(new_setpoint),setAngles(Output),
# 				SetTunings(Kp,Ki,Kd), SetSampleTime(NewSampleTime), 
# 				SetOutputLimits(Min,Max), Initialize(), coordinateTransform(xy)
#				   [ Comma separated list of functions in this file ]
# Global variables: client_id, setpoint=[],vision_sensor_handle,revolute_handle,kp,ki,kd,outMax,outMin,lastTime,error,summation
			# , Input, lastInput, ITerm, SampleTime, Output, lastOutput
					# [ List of global variables defined in this file ]


####################### IMPORT MODULES #########################
## You are not allowed to make any changes in this section.   ##
## You have to implement this task with the six available	 ##
## modules for this task (numpy,opencv,os,sys,traceback,time) ##
################################################################
import numpy as np
import cv2
import os, sys
import traceback
import time
##############################################################

# Importing the sim module for Remote API connection with CoppeliaSim
try:
	import sim
	
except Exception:
	print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
	print('\n[WARNING] Make sure to have following files in the directory:')
	print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
	sys.exit()




# Global variable "client_id" for storing ID of starting the CoppeliaSim Remote connection
# NOTE: DO NOT change the value of this "client_id" variable here
client_id = -1

# Global list "setpoint" for storing target position of ball on the platform/top plate
# The zeroth element stores the x pixel and 1st element stores the y pixel
# NOTE: DO NOT change the value of this "setpoint" list
setpoint = [1024,256]

# Global variable "vision_sensor_handle" to store handle for Vision Sensor
# NOTE: DO NOT change the value of this "vision_sensor_handle" variable here
vision_sensor_handle = 0

# You can add your global variables here
##############################################################


outMax=60
outMin=-60
kp=np.array([0.018,0.018],dtype='float64')
ki=np.array([0.001,0.001],dtype='float64')#ki=ki*SampleTime
kd=np.array([0.135,0.135],dtype='float64')#kd=kd/SampleTime
lastTime=0
SampleTime = 0.01 #0.01 sec
##############################################################



################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.	  ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.						 ##
##############################################################
def setAngles(client_id,revolute_handle,Output):
	# print("Output=",Output)
	#setting output to joints/motors
	#This can be useful if you need to send several values to CoppeliaSim that should be received and evaluated at the same time. 
	_=sim.simxPauseCommunication(client_id,True)
	# Output[0]=(-1)*Output[0]
	# Output[1]=(-1)*Output[1]
	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[0],-Output[0]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[0],-Output[0]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[7],-Output[0]*np.pi/180,sim.simx_opmode_oneshot)

	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[2],Output[0]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[3],Output[0]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[4],Output[0]*np.pi/180,sim.simx_opmode_oneshot)
	
	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[1],Output[1]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[1],Output[1]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[2],Output[1]*np.pi/180,sim.simx_opmode_oneshot)
	
	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[3],-Output[1]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[5],-Output[1]*np.pi/180,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[6],-Output[1]*np.pi/180,sim.simx_opmode_oneshot)

	# print( -Output[0]*np.pi/180,"-Output[0]*np.pi/180" )
	# print( Output[0]*np.pi/180,"Output[0]*np.pi/180" )
	# print( Output[1]*np.pi/180,"Output[1]*np.pi/180" )
	# print( -Output[1]*np.pi/180,"-Output[1]*np.pi/180" )
	
	_=sim.simxPauseCommunication(client_id,False)
	#returnCode,position=sim.simxGetJointPosition(client_id,revolute_handle[0],sim.simx_opmode_streaming)
	#print(position*180/np.pi)
	#simxSynchronousTrigger(client_id)
	
	
# def SetTunings(Kp,Ki,Kd):
# 	#changing the values of kp,ki,kd
# 	global kp,ki,kd,SampleTime
# 	kp = Kp
# 	ki = Ki * SampleTime
# 	kd = Kd / SampleTime

# def SetSampleTime(NewSampleTime):
	
# 	global SampleTime,ki,kd
# 	if (NewSampleTime > 0):
# 		ratio  = NewSampleTime/ SampleTime
# 		ki *= ratio
# 		kd /= ratio
# 		SampleTime = NewSampleTime
		
# def SetOutputLimits(Min,Max):
# 	global outMin,outMax
# 	if(Min > Max):
# 		return
# 	outMin = Min
# 	outMax = Max
# 	#for i in range(len(Output)):
# 	#	if(Output[i] > outMax):
# 	#		Output[i] = outMax
# 	#	elif(Output[i] < outMin): 
# 	#		Output[i] = outMin
		
# 	for i in range(len(ITerm)):
# 		if(ITerm[i]> outMax):
# 			ITerm[i]= outMax
# 		elif(ITerm[i]< outMin): 
# 			ITerm[i]= outMin	
# def Initialize():
# 	global lastInput,ITerm,Input,outMax,outMin
# 	lastInput = Input
# 	ITerm = Output
# 	for i in range(len(ITerm)):
# 		if(ITerm[i]> outMax):
# 			ITerm[i]= outMax
# 		elif(ITerm[i]< outMin):
# 			ITerm[i]= outMin
##############################################################



def init_setup(rec_client_id,table_number):
	"""
	Purpose:
	---
	This function should:
	
	1. Get all the required handles from the CoppeliaSim scene and store them in global variables.
	2. Initialize the vision sensor in 'simx_opmode_streaming' operation mode (if required). 
	   Teams are allowed to choose the appropriate the oeration mode depending on their code and logic.
	Input Arguments:
	---
	`rec_client_id` 	:  [ integer ]
		the client_id generated from start connection remote API in Task 2A, should be stored in a global variable
	
	Returns:
	---
	None
	
	Example call:
	---
	init_setup()
	
	"""
	# since client_id is defined in task_2a.py file, it needs to be assigned here as well.
	client_id = rec_client_id
	revolute_handle=[-1,-1,-1,-1,-1,-1,-1,-1]
	##############	ADD YOUR CODE HERE	##############
	#The function is blocking. While in synchronous operation mode, the client application is in charge of triggering the next simulation step.
	#_=sim.simxSynchronous(client_id,1)
	#saving andles to global variables
	_,revolute_handle[0]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_1",sim.simx_opmode_blocking)
	_,revolute_handle[1]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_2",sim.simx_opmode_blocking)
	_,revolute_handle[2]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_3",sim.simx_opmode_blocking)
	_,revolute_handle[3]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_4",sim.simx_opmode_blocking)
	_,revolute_handle[4]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_5",sim.simx_opmode_blocking)
	_,revolute_handle[5]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_6",sim.simx_opmode_blocking)
	_,revolute_handle[6]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_7",sim.simx_opmode_blocking)
	_,revolute_handle[7]=sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t"+table_number+"_8",sim.simx_opmode_blocking)
	_, vision_sensor_handle = sim.simxGetObjectHandle(client_id, 'vision_sensor_'+table_number, sim.simx_opmode_blocking)

	# _=sim.simxPauseCommunication(client_id,True)
	
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[0],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[7],0,sim.simx_opmode_oneshot)
	
	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[2],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[3],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[4],0,sim.simx_opmode_oneshot)
	
	
	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[1],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[2],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[1],0,sim.simx_opmode_oneshot)


	
	
	# _=sim.simxSetJointTargetPosition(client_id,revolute_handle[3],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[5],0,sim.simx_opmode_oneshot)
	_=sim.simxSetJointTargetPosition(client_id,revolute_handle[6],0,sim.simx_opmode_oneshot)
	
	# _=sim.simxPauseCommunication(client_id,False)
	
	#setting all angles target pposition to [0,0]
	setAngles(client_id,revolute_handle,[0,0]) 
	# print(sensor_handle, "sensor_handle")
	#staring vision sensor image in sim.simx_opmode_streaming
	_, _, _ = sim.simxGetVisionSensorImage(client_id,vision_sensor_handle, 0, sim.simx_opmode_streaming)  # streamig may need change
	
	#Storing time when the simulation started in variable init_simulation_time
	_,init_simulation_time_string=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)
	#print("init_simulation_time_string=",(float)init_simulation_time_string)
	_,_ = sim.simxGetPingTime(client_id)
	#print(vision_sensor_handle,revolute_handle)
	return revolute_handle,vision_sensor_handle
	##################################################

def coordinateTransform(xy):
	# as our servos are capable of moving the ball along the diagonals, we have to covert the 
	# performing coordinate transformation from x,y to diagonal axes
	theta=np.pi/4
	transformed=[np.cos(theta)*xy[0]+np.sin(theta)*xy[1],-np.sin(theta)*xy[0]+np.cos(theta)*xy[1]]
	return np.array(transformed,dtype='float64')

def control_logic(setpoint,client_id,center_x,center_y,ITerm,lastInput,lastTime,Input,lastOutput,summation,Output):
	"""
	Purpose:
	---
	This function should implement the control logic to balance the ball at a particular setpoint on the table.
	The orientation of the top table should "ONLY" be controlled by the servo motor as we would expect in a 
	practical scenario.
	Hence "ONLY" the shaft of the servo motor or in other words the revolute joint between servo and servo fin 
	should have 'motor enabled' and 'control loop enabled option' checked. Refer documentation for further understanding of 
	these options.
	This function should use the necessary Legacy Python Remote APIs to control the revolute joints.
	NOTE: In real life, a 180 degree servo motor can rotate between -90 to +90 degrees or -1.57 to 1.57 radians only. 
		  Hence the command to be sent to servo motor should be between this range only. When the top plate is parallel to
		  base plate, the revolute joint between servo and servo fin should be at 0 degrees orientation. Refer documentation
		  for further understanding.
	NOTE: Since the simulation is dynamic in nature there should not by any bottlenecks in this code due to which the 
		  processing may take a lot of time. As a result 'control_logic' function should be called in every iteration of 
		  the while loop. Use global variables instead of reinitialising the varibles used in this function.
	
	Input Arguments:
	---
	`center_x` 	:  [ int ]
		the x centroid of the ball
	`center_y` 	:  [ int ]
		the y centroid of the ball
	
	Returns:
	---
	None
	
	Example call:
	---
	control_logic(center_x,center_y)
	
	"""
	##############	ADD YOUR CODE HERE	##############
	#taking handles from global variables
	#the pid computes using the coordinates and setpoint and returns us the value
	# print("Centroid=",center_x," ",center_y," setpoint=",setpoint)
	
	#global variables
	global kp,ki,kd,outMin,outMax,SampleTime
	#IMPORTANT: most the variables here are a list having two elements 
	# representing 2 independent linear unit
	#now = time.time()
	#print(now)
	return_code_signal,now=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
	
	if(return_code_signal == 0):
		now=float(now)
		#print("Now=",now)
	else:
		return
	timeChange=now-lastTime  

	#print("TimeChange=",timeChange)
	if(timeChange>=SampleTime):
		#Compute all the working error variables
		#transform of coordinates

		# We ahve divide the 2D plane problem 2 independent linear problems 
		# and then applied pid independently on them
		
		Input=coordinateTransform([center_x,center_y])
		#calculation of error
		setpoint=np.array(setpoint,dtype="float64")
		error=setpoint-np.array([center_x,center_y],dtype="float64")
		#matrix multiplication of error and coordinate transformation matrix
		transform=np.array([[np.cos(np.pi/4),-np.sin(np.pi/4)],[np.sin(np.pi/4),np.cos(np.pi/4)]],dtype="float64")
		error=np.dot(error,transform)
		# print("Error=",error[0]*error[0]+error[1]*error[1])

		#calclating integral term ,ki*error*delta t,here assuming that delta t already multiplied in ki 

		# print(timeChange)
		# here summation means the summation of all previous error
		# we are adding the ITerm only when the ball is close to setpoint

		if(error[0]*error[0]+error[1]*error[1]<8000):
			ITerm= ki*(summation)*timeChange
			summation+=error
			kd=np.array([0.12,0.12],dtype='float64')
		if(error[0]*error[0]+error[1]*error[1]<1500):
			kd=np.array([0.2,0.2],dtype='float64')

		dInput = (Input - lastInput)
		for i in range(2):
			#dealing with windup
			if(ITerm[i]> outMax):
				ITerm[i]= outMax
			elif(ITerm[i]< outMin):
				ITerm[i]= outMin
			#Compute PID Output, here ki has already been multiplied by sampleTime i.e. delta t
			Output[i] = (float)(kp[i] * error[i] + ITerm[i]- (float)((kd[i] * dInput[i]))/timeChange)
			# print(kp[i] * error[i] + ITerm[i]- kd[i] * dInput[i]/timeChange)
			if(Output[i]> outMax):
				Output[i] = outMax
			elif(Output[i] < outMin):
				Output[i] = outMin
		# print("Output=",Output)	  
		#Remember some variables for next time
		lastInput = Input
		lastTime = now
		lastOutput=Output
		setAngles(Output)
		#  In case value of kd has changed
		kd=np.array([0.135,0.135],dtype='float64')
    return ITerm,lastInput,lastTime,Input,lastOutput,summation,Output
	##################################################

# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:	change_setpoint
#		Inputs:	list of new setpoint-
#						new_setpoint=[x_pixel,y_pixel]
#	   Outputs:	None
#	   Purpose:	The function updates the value of global "setpoint" list after every 15 seconds of simulation time.
#					This will be ONLY called by executable file. 
# def change_setpoint(new_setpoint):

# 	global setpoint
# 	setpoint=new_setpoint[:]


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:	main
#		Inputs:	None
#	   Outputs:	None
#	   Purpose:	This part of the code is only for testing your solution. The function does the following:
# - imports 'task_1b' file as module
# - imports 'task_1a_part1' file as module
#						- imports 'task_2a' file as module
# - calls init_remote_api_server() function in 'task_2a' to connect with CoppeliaSim Remote API server
# - then calls start_simulation() function in 'task_2a' to start the simulation
#- then calls init_setup() function to store the required handles in respective global variables and complete initializations if required
# - then calls get_vision_sensor_image() function in 'task_2a' to capture an image from the Vision Sensor in CoppeliaSim scene
# - If the return code is 'simx_return_ok':
# - then calls transform_vision_sensor_image() function in 'task_2a' to transform the captured image
#   to a format compatible with OpenCV. 
# - then the transformed image is given as input and Perspective Transform is applied
# by calling applyPerspectiveTransform function	from 'task_1b'
# - then the output of warped_img is given to 'scan_image' function from 'task_1a_part1'
# - then calls control_logic() function to command the servo motors

# NOTE: Write your solution ONLY in the space provided in the above functions. Main function should not be edited.

if __name__ == "__main__":

	# Import 'task_1b.py' file as module
	try:
		import task_1b

	except ImportError:
		print('\n[ERROR] task_1b.py file is not present in the current directory.')
		print('Your current directory is: ', os.getcwd())
		print('Make sure task_1b.py is present in this current directory.\n')
		sys.exit()
		
	except Exception as e:
		print('Your task_1b.py throwed an Exception. Kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()
	
	# Import 'task_1a_part1.py' file as module
	try:
		import task_1a_part1

	except ImportError:
		print('\n[ERROR] task_1a_part1.py file is not present in the current directory.')
		print('Your current directory is: ', os.getcwd())
		print('Make sure task_1a_part1.py is present in this current directory.\n')
		sys.exit()
		
	except Exception as e:
		print('Your task_1a_part1.py throwed an Exception. Kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()
	
	# Import 'task_2a.py' file as module
	try:
		import task_2a

	except ImportError:
		print('\n[ERROR] task_2a.py file is not present in the current directory.')
		print('Your current directory is: ', os.getcwd())
		print('Make sure task_2a.py is present in this current directory.\n')
		sys.exit()
		
	except Exception as e:
		print('Your task_2a.py throwed an Exception. Kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()

	# Initiate the Remote API connection with CoppeliaSim server
	print('\nConnection to CoppeliaSim Remote API Server initiated.')
	print('Trying to connect to Remote API Server...')
	# print("Start=",time.time())
	try:
		client_id = task_2a.init_remote_api_server()
		# print("init_remote_api_server()=",time.time())
		if (client_id != -1):
			print('\nConnected successfully to Remote API Server in CoppeliaSim!')

			# Starting the Simulation
			try:
				return_code = task_2a.start_simulation()
				# print("start_simulation()=",time.time())
				if (return_code == sim.simx_return_novalue_flag):
					print('\nSimulation started correctly in CoppeliaSim.')
					
					# Storing the required handles in respective global variables.
					try:
						init_setup(client_id)
					except Exception:
						print('\n[ERROR] Your init_setup() function throwed an Exception. Kindly debug your code!')
						print('Stop the CoppeliaSim simulation manually if started.\n')
						traceback.print_exc(file=sys.stdout)
						print()
						sys.exit()

				else:
					print('\n[ERROR] Failed starting the simulation in CoppeliaSim!')
					print('start_simulation function in task_2a.py is not configured correctly, check the code!')
					print()
					sys.exit()

			except Exception:
				print('\n[ERROR] Your start_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed connecting to Remote API server!')
			print('[WARNING] Make sure the CoppeliaSim software is running and')
			print('[WARNING] Make sure the Port number for Remote API Server is set to 19997.')
			print('[ERROR] OR init_remote_api_server function in task_2a.py is not configured correctly, check the code!')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your init_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually if started.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
	
	# Initialising the center_x and center_y variable to the current position of the ball
	# center_x = 1063
	# center_y = 1063
	center_x = 640
	center_y = 640
	
	init_simulation_time = 0
	curr_simulation_time = 0

	# Storing time when the simulation started in variable init_simulation_time
	return_code_signal,init_simulation_time_string=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)
	# print("simxGetStringSignal()=",time.time())
	if(return_code_signal==0):
		init_simulation_time=float(init_simulation_time_string)
	lastInput = coordinateTransform([center_x,center_y])
	# Running the coppeliasim simulation for 15 seconds
	flag=False
	while(curr_simulation_time - init_simulation_time <=15):
		# x=time.time()
		# print("Starting Coppeliasim Loop, time=",x)
		return_code_signal,curr_simulation_time_string=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
		# print(init_simulation_time,curr_simulation_time)
		# print("simxGetStringSignal()=",time.time()-x)
		# x=time.time()
		if(return_code_signal == 0):
			curr_simulation_time=float(curr_simulation_time_string)
		
		try:
			vision_sensor_image, image_resolution, return_code = task_2a.get_vision_sensor_image(vision_sensor_handle)
			# print("get_vision_sensor_image()=",time.time()-x)
			# x=time.time()
			if ((return_code == sim.simx_return_ok) and (len(image_resolution) == 2) and (len(vision_sensor_image) > 0)):
				print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')

				# Get the transformed vision sensor image captured in correct format
				try:
					transformed_image = task_2a.transform_vision_sensor_image(vision_sensor_image, image_resolution)
					# print("transform_vision_sensor_image()=",time.time()-x)
					# x=time.time()
					if (type(transformed_image) is np.ndarray):

						# Get the resultant warped transformed vision sensor image after applying Perspective Transform
						try:
							warped_img = task_1b.applyPerspectiveTransform(transformed_image)
							
							if (type(warped_img) is np.ndarray):
								# print("applyPerspectiveTransform()=",time.time()-x)
								# x=time.time()
								# Get the 'shapes' dictionary by passing the 'warped_img' to scan_image function
								try:
									shapes = task_1a_part1.scan_image(warped_img)
									# print("scan_image()=",time.time()-x)
									# x=time.time()
									if (type(shapes) is dict and shapes!={}):
										print('\nShapes detected by Vision Sensor are: ')
										print(shapes)
										# Storing the detected x and y centroid in center_x and center_y variable repectively
										center_x = shapes['Circle'][1]
										center_y = shapes['Circle'][2]
									elif(type(shapes) is not dict):
										print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.')
										print('Stop the CoppeliaSim simulation manually.')
										print()
										sys.exit()
								
								except Exception:
									print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception. Kindly debug your code!')
									print('Stop the CoppeliaSim simulation manually.\n')
									traceback.print_exc(file=sys.stdout)
									print()
									sys.exit()
							
							else:
								print('\n[ERROR] applyPerspectiveTransform function is not configured correctly, check the code.')
								print('Stop the CoppeliaSim simulation manually.')
								print()
								sys.exit()
						
						except Exception:
							print('\n[ERROR] Your applyPerspectiveTransform function in task_1b.py throwed an Exception. Kindly debug your code!')
							print('Stop the CoppeliaSim simulation manually.\n')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()

					else:
						print('\n[ERROR] transform_vision_sensor_image function in task_2a.py is not configured correctly, check the code.')
						print('Stop the CoppeliaSim simulation manually.')
						print()
						sys.exit()

				except Exception:
					print('\n[ERROR] Your transform_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
					print('Stop the CoppeliaSim simulation manually.\n')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
			
			try:
				# control_logic(center_x,center_y)
				if(flag):
					control_logic(center_x,center_y)
				else:
					lastInput=coordinateTransform([center_x,center_y])
					flag=True
			except:
				print('\n[ERROR] Your control_logic function throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()

		except Exception:
			print('\n[ERROR] Your get_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

	# Ending the Simulation
	try:
		return_code = task_2a.stop_simulation()
		
		if (return_code == sim.simx_return_novalue_flag):
			print('\nSimulation stopped correctly.')

			# Stop the Remote API connection with CoppeliaSim server
			try:
				task_2a.exit_remote_api_server()

				if (task_2a.start_simulation() == sim.simx_return_initialize_error_flag):
					print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')

				else:
					print('\n[ERROR] Failed disconnecting from Remote API server!')
					print('[ERROR] exit_remote_api_server function in task_2a.py is not configured correctly, check the code!')

			except Exception:
				print('\n[ERROR] Your exit_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed stopping the simulation in CoppeliaSim server!')
			print('[ERROR] stop_simulation function in task_2a.py is not configured correctly, check the code!')
			print('Stop the CoppeliaSim simulation manually.')
		
		print()
		sys.exit()

	except Exception:
		print('\n[ERROR] Your stop_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
