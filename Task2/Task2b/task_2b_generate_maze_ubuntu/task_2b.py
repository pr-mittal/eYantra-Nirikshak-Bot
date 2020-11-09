'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 2B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_2b.py
# Functions:		init_remote_api_server, exit_remote_api_server, get_vision_sensor_image,
# 					transform_vision_sensor_image, send_data
# 					[ Comma separated list of functions in this file ]
# Global variables:	client_id
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the available       ##
## modules for this task (numpy,opencv,os,sys,platform      ##
## traceback and math )                                     ##
##############################################################
import cv2
import numpy as np
import os, sys, platform
import traceback
import math
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


##############################################################

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################





##############################################################


def init_remote_api_server():

	"""
	Purpose:
	---
	This function should first close any open connections and then start
	communication thread with server i.e. CoppeliaSim.

	NOTE: In this Task, do not call the exit_remote_api_server function in case of failed connection to the server.
	The test_task_2a executable script will handle that condition.
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	`client_id` 	:  [ integer ]
		the client_id generated from start connection remote API, it should be stored in a global variable
	
	Example call:
	---
	client_id = init_remote_api_server()
	
	NOTE: This function will be automatically called by test_task_2a executable before starting the simulation.
	"""

	global client_id

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return client_id


def get_vision_sensor_image():
	
	"""
	Purpose:
	---
	This function should first get the handle of the Vision Sensor object from the scene.
	After that it should get the Vision Sensor's image array from the CoppeliaSim scene.

	Input Arguments:
	---
	None
	
	Returns:
	---
	`vision_sensor_image` 	:  [ list ]
		the image array returned from the get vision sensor image remote API
	`image_resolution` 		:  [ list ]
		the image resolution returned from the get vision sensor image remote API
	`return_code` 			:  [ integer ]
		the return code generated from the remote API
	
	Example call:
	---
	vision_sensor_image, image_resolution, return_code = get_vision_sensor_image()

	NOTE: This function will be automatically called by test_task_2a executable at regular intervals.
	"""

	global client_id

	vision_sensor_image = []
	image_resolution = []
	return_code = 0

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return vision_sensor_image, image_resolution, return_code


def transform_vision_sensor_image(vision_sensor_image, image_resolution):

	"""
	Purpose:
	---
	Transforms the image data returned by simxGetVisionSensorImage into a numpy
	array that is possible to process using OpenCV library.

	This function should:
	1. First convert the vision_sensor_image list to a NumPy array with data-type as uint8.
	2. Since the image returned from Vision Sensor is in the form of a 1-D (one dimensional) array,
	the new NumPy array should then be resized to a 3-D (three dimensional) NumPy array.
	3. Change the color of the new image array from BGR to RGB.
	4. Flip the resultant image array about the X-axis.
	The resultant image NumPy array should be returned.
	
	Input Arguments:
	---
	`vision_sensor_image` 	:  [ list ]
		the image array returned from the get vision sensor image remote API
	`image_resolution` 		:  [ list ]
		the image resolution returned from the get vision sensor image remote API
	
	Returns:
	---
	`transformed_image` 	:  [ numpy array ]
		the resultant transformed image array after performing above 4 steps
		that can be processed further using OpenCV library
	
	Example call:
	---
	transformed_image = transform_vision_sensor_image(vision_sensor_image, image_resolution)
	
	NOTE: This function will be automatically called by test_task_2a executable at regular intervals.
	"""

	transformed_image = None

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################
	
	return transformed_image


def send_data(maze_array):
	
	"""
	Purpose:
	---
	Sends data to CoppeliaSim via Remote API.

	Input Arguments:
	---
	`maze_array` :    [ nested list of lists ]
		encoded maze in the form of a 2D array returned by detectMaze() function
	
	Returns:
	---
	`return_code` 	:  [ integer ]
		the return code generated from the call script function remote API
	
	Example call:
	---
	send_data(maze_array)
	
	NOTE: You might want to study this link to understand simx.callScriptFunction() better
	https://www.coppeliarobotics.com/helpFiles/en/remoteApiExtension.htm
	"""

	global client_id

	return_code = -1

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return return_code


def exit_remote_api_server():
	
	"""
	Purpose:
	---
	This function should wait for the last command sent to arrive at the Coppeliasim server
	before closing the connection and then end the communication thread with server
	i.e. CoppeliaSim using simxFinish Remote API.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	exit_remote_api_server()
	
	NOTE: This function will be automatically called by test_task_2a executable after ending the simulation.
	"""

	global client_id

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function does the following:
#                   	- takes maze00.jpg as input
#                       - applies the Perspective transform and encodes the maze in the form of a 2D array by
#                         calling the detectMaze() function (same as Task 1B)
#                       - connects with the remote API server (CoppeliaSim scene)
#                       - starts the simulation
#                       - receives the output of the Vision Sensor in the CoppeliaSim scene
#                       - saves the output of vision sensor as an image
#                       - stops the simulation
#                       - Disconnects with the remote API server
#                   It then asks the whether to repeat the same above steps on all maze images present in 
#                   'test_cases' folder or not. Write your solution ONLY in the space provided in the 
#                   transform_vision_sensor_image() and send_data() functions.

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
		print('Your task_1b.py throwed an Exception, kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()
	
	# Initiate the Remote API connection with CoppeliaSim server
	print('\nConnection to CoppeliaSim Remote API Server initiated.')
	print('Trying to connect to Remote API Server...')

	try:
		client_id = init_remote_api_server()

		if (client_id != -1):
			print('\nConnected successfully to Remote API Server in CoppeliaSim!')
		
		else:
			print('\n[ERROR] Failed connecting to Remote API server!')
			print('[WARNING] Make sure the CoppeliaSim software is running and')
			print('[WARNING] Make sure the Port number for Remote API Server is set to 19997.')
			print('[ERROR] OR init_remote_api_server function is not configured correctly, check the code!')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your init_remote_api_server function throwed an Exception, kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually if started.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
	
	# Flag to check whether maze array is generated or not, initially set to 0
	maze_array_generated_flag = 0

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path directory to 'generated_images' folder 
	generated_dir_path = 'generated_images/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	if os.path.exists(img_file_path):
		# print('\nFound maze0' + str(file_num) + '.jpg')
		pass
	
	else:
		print('\n[ERROR] maze0' + str(file_num) + '.jpg not found. Make sure "test_cases" folder is present in current directory.')
		print('Your current directory is: ', os.getcwd())
		sys.exit()

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	if type(input_img) is np.ndarray:

		try:
			# get the resultant warped maze image after applying Perspective Transform
			warped_img = task_1b.applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				try:
					# get the encoded maze in the form of a 2D array
					maze_array = task_1b.detectMaze(warped_img)

					if (type(maze_array) is list) and (len(maze_array) == 10):
						print('\nEncoded Maze Array = %s' % (maze_array))
						print('\n============================================')

						# Flag for maze array generated updated to 1
						maze_array_generated_flag = 1
					
					else:
						print('\n[ERROR] maze_array returned by detectMaze function in \'task_1b.py\' is not returning maze array in expected format!, check the code.')
						print()
						sys.exit()
				
				except Exception:
					print('\n[ERROR] Your detectMaze function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
			
			else:
				print('\n[ERROR] applyPerspectiveTransform function in \'task_1b.py\' is not returning the warped maze image in expected format!, check the code.')
				print()
				sys.exit()

		except Exception:
			print('\n[ERROR] Your applyPerspectiveTransform function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

	else:
		print('\n[ERROR] maze0' + str(file_num) + '.jpg was not read correctly, something went wrong!')
		print()
		sys.exit()

	# Check if connected to Remote API server and maze array has been generated successfully
	if ((client_id != -1) and (maze_array_generated_flag == 1)):

		try:
			# Send maze array data to CoppeliaSim via Remote API
			return_code = send_data(maze_array)

			if (return_code == sim.simx_return_ok):

				# Start the simulation
				return_code = sim.simxStartSimulation(client_id, sim.simx_opmode_oneshot)

				# Making sure that last command sent out had time to arrive
				sim.simxGetPingTime(client_id)
				
				if ((return_code == sim.simx_return_novalue_flag) or (return_code == sim.simx_return_ok)):
					print('\nSimulation started correctly in CoppeliaSim.')

				time.sleep(2)

				try:
					# Get image array and its resolution from Vision Sensor in ComppeliaSim scene
					vision_sensor_image, image_resolution, return_code = get_vision_sensor_image()

					if ((return_code == sim.simx_return_ok) and (len(image_resolution) == 2) and (len(vision_sensor_image) > 0)):
						print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')
						
						# Get the transformed vision sensor image captured in correct format
						try:
							transformed_image = transform_vision_sensor_image(vision_sensor_image, image_resolution)

							if (type(transformed_image) is np.ndarray):
								# Save generated maze image in 'generated_images' folder
								generated_img_file_path = generated_dir_path + 'result_maze0' + str(file_num) + '.jpg'

								# Create the 'generated_images' folder and save the transformed image
								if os.path.isdir(generated_dir_path) == True:
									pass

								else:
									os.mkdir(generated_dir_path)
								
								return_code = cv2.imwrite(generated_img_file_path, transformed_image)
								
								if return_code == True:
									print('\nTransformed maze image from CoppeliaSim: ' + str(generated_img_file_path) + ' was saved in \'generated_images\' folder successfully!')

								else:
									print('\n[ERROR] Failed to save Transformed maze image from CoppeliaSim in \'generated_images\' folder.')

								# Stop the simulation
								return_code = sim.simxStopSimulation(client_id, sim.simx_opmode_oneshot)

								# Making sure that last command sent out had time to arrive
								sim.simxGetPingTime(client_id)

								if ((return_code == sim.simx_return_novalue_flag) or (return_code == sim.simx_return_ok)):
									print('\nSimulation stopped correctly.')

									time.sleep(2)

									# Stop the Remote API connection with CoppeliaSim server
									try:
										exit_remote_api_server()

										if (sim.simxStartSimulation(client_id, sim.simx_opmode_oneshot) == sim.simx_return_initialize_error_flag):
											print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')

										else:
											print('\n[ERROR] Failed disconnecting from Remote API server!')
											print('[ERROR] exit_remote_api_server function is not configured correctly, check the code!')

									except Exception:
										print('\n[ERROR] Your exit_remote_api_server function throwed an Exception, kindly debug your code!')
										print('Stop the CoppeliaSim simulation manually.\n')
										traceback.print_exc(file=sys.stdout)
										print()
										sys.exit()
						
						except Exception:
							print('\n[ERROR] Your transform_vision_sensor_image function throwed an Exception, kindly debug your code!')
							print('Stop the CoppeliaSim simulation manually.\n')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()
				
				except Exception:
					print('\n[ERROR] Your get_vision_sensor_image function throwed an Exception, kindly debug your code!')
					print('Stop the CoppeliaSim simulation manually.\n')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
			
		except Exception:
			print('\n[ERROR] Your send_data function throwed an Exception, kindly debug your code!')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		try:
			client_id = init_remote_api_server()

			if (client_id != -1):
				print('\nConnected successfully to Remote API Server in CoppeliaSim!')
			
			else:
				print('\n[ERROR] Failed connecting to Remote API server!')
				print('[WARNING] Make sure the CoppeliaSim software is running and')
				print('[WARNING] Make sure the Port number for Remote API Server is set to 19997.')
				print('[ERROR] OR init_remote_api_server function is not configured correctly, check the code!')
				print()
				sys.exit()

		except Exception:
			print('\n[ERROR] Your init_remote_api_server function throwed an Exception, kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually if started.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()
		
		for file_num in range(1,9):

			# Reset the flag to check whether maze array is generated or not to 0
			maze_array_generated_flag = 0

			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			if os.path.exists(img_file_path):
				# print('\nFound maze0' + str(file_num) + '.jpg')
				pass
			
			else:
				print('\n[ERROR] maze0' + str(file_num) + '.jpg not found. Make sure "test_cases" folder is present in current directory.')
				print('Your current directory is: ', os.getcwd())
				sys.exit()

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# read the image file
			input_img = cv2.imread(img_file_path)

			if type(input_img) is np.ndarray:

				try:
					# get the resultant warped maze image after applying Perspective Transform
					warped_img = task_1b.applyPerspectiveTransform(input_img)

					if type(warped_img) is np.ndarray:

						try:
							# get the encoded maze in the form of a 2D array
							maze_array = task_1b.detectMaze(warped_img)

							if (type(maze_array) is list) and (len(maze_array) == 10):
								print('\nEncoded Maze Array = %s' % (maze_array))
								print('\n============================================')

								# Flag for maze array generated updated to 1
								maze_array_generated_flag = 1
							
							else:
								print('\n[ERROR] maze_array returned by detectMaze function in \'task_1b.py\' is not returning maze array in expected format!, check the code.')
								print()
								sys.exit()
						
						except Exception:
							print('\n[ERROR] Your detectMaze function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()
					
					else:
						print('\n[ERROR] applyPerspectiveTransform function in \'task_1b.py\' is not returning the warped maze image in expected format!, check the code.')
						print()
						sys.exit()

				except Exception:
					print('\n[ERROR] Your applyPerspectiveTransform function in \'task_1b.py\' throwed an Exception, kindly debug your code!')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()

			else:
				print('\n[ERROR] maze0' + str(file_num) + '.jpg was not read correctly, something went wrong!')
				print()
				sys.exit()

			# Check if connected to Remote API server and maze array has been generated successfully
			if ((client_id != -1) and (maze_array_generated_flag == 1)):

				try:
					# Send maze array data to CoppeliaSim via Remote API
					return_code = send_data(maze_array)

					if (return_code == sim.simx_return_ok):

						# Start the simulation
						return_code = sim.simxStartSimulation(client_id, sim.simx_opmode_oneshot)

						# Making sure that last command sent out had time to arrive
						sim.simxGetPingTime(client_id)
						
						if ((return_code == sim.simx_return_novalue_flag) or (return_code == sim.simx_return_ok)):
							print('\nSimulation started correctly in CoppeliaSim.')

						time.sleep(2)

						try:
							# Get image array and its resolution from Vision Sensor in ComppeliaSim scene
							vision_sensor_image, image_resolution, return_code = get_vision_sensor_image()

							if ((return_code == sim.simx_return_ok) and (len(image_resolution) == 2) and (len(vision_sensor_image) > 0)):
								print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')
								
								# Get the transformed vision sensor image captured in correct format
								try:
									transformed_image = transform_vision_sensor_image(vision_sensor_image, image_resolution)

									if (type(transformed_image) is np.ndarray):
										# Save generated maze image in 'generated_images' folder
										generated_img_file_path = generated_dir_path + 'result_maze0' + str(file_num) + '.jpg'

										# Create the 'generated_images' folder and save the transformed image
										if os.path.isdir(generated_dir_path) == True:
											pass

										else:
											os.mkdir(generated_dir_path)
										
										return_code = cv2.imwrite(generated_img_file_path, transformed_image)
										
										if return_code == True:
											print('\nTransformed maze image from CoppeliaSim: ' + str(generated_img_file_path) + ' was saved in \'generated_images\' folder successfully!')

										else:
											print('\n[ERROR] Failed to save Transformed maze image from CoppeliaSim in \'generated_images\' folder.')

										# Stop the simulation
										return_code = sim.simxStopSimulation(client_id, sim.simx_opmode_oneshot)

										# Making sure that last command sent out had time to arrive
										sim.simxGetPingTime(client_id)
										
										if ((return_code == sim.simx_return_novalue_flag) or (return_code == sim.simx_return_ok)):
											print('\nSimulation stopped correctly.')
										
										time.sleep(2)
								
								except Exception:
									print('\n[ERROR] Your transform_vision_sensor_image function throwed an Exception, kindly debug your code!')
									print('Stop the CoppeliaSim simulation manually.\n')
									traceback.print_exc(file=sys.stdout)
									print()
									sys.exit()
						
						except Exception:
							print('\n[ERROR] Your get_vision_sensor_image function throwed an Exception, kindly debug your code!')
							print('Stop the CoppeliaSim simulation manually.\n')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()
					
				except Exception:
					print('\n[ERROR] Your send_data function throwed an Exception, kindly debug your code!')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
		
		# Stop the Remote API connection with CoppeliaSim server
		try:
			exit_remote_api_server()

			if (sim.simxStartSimulation(client_id, sim.simx_opmode_oneshot) == sim.simx_return_initialize_error_flag):
				print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')

			else:
				print('\n[ERROR] Failed disconnecting from Remote API server!')
				print('[ERROR] exit_remote_api_server function is not configured correctly, check the code!')

		except Exception:
			print('\n[ERROR] Your exit_remote_api_server function throwed an Exception, kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()
	
	else:
		print('')
		


