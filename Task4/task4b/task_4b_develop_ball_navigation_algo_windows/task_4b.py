'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 4B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Filename:         task_4b.py
# Functions:        calculate_path_from_maze_image, send_data_to_draw_path, 
# 					convert_path_to_pixels, traverse_path
#                   [ Comma separated list of functions in this file ]
# Global variables: client_id, setpoint, start_coord, end_coord
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy,opencv,os,sys,traceback)    ##
##############################################################
import numpy as np
import cv2
import os, sys
import traceback
import time
import math
##############################################################

# Importing the sim module for Remote API connection with CoppeliaSim
try:
	import sim
	
except Exception:
	print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
	print('\n[WARNING] Make sure to have following files in the directory:')
	print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
	sys.exit()

#Import 'task_1b.py' file as module
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

# Import 'task_2b.py' file as module
try:
	import task_2b

except ImportError:
	print('\n[ERROR] task_2b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_2b.py is present in this current directory.\n')
	sys.exit()
	
except Exception as e:
	print('Your task_2b.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	sys.exit()

# Import 'task_3.py' file as module
try:
	import task_3

except ImportError:
	print('\n[ERROR] task_3.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_3.py is present in this current directory.\n')
	sys.exit()
	
except Exception as e:
	print('Your task_3.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	sys.exit()


# Import 'task_4a.py' file as module
try:
	import task_4a

except ImportError:
	print('\n[ERROR] task_4a.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_4a.py is present in this current directory.\n')
	sys.exit()
	
except Exception as e:
	print('Your task_4a.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	sys.exit()

# Global variable "client_id" for storing ID of starting the CoppeliaSim Remote connection
# NOTE: DO NOT change the value of this "client_id" variable here
client_id = -1

# Global list "setpoint" for storing target position of ball on the platform/top plate
# The 0th element stores the x pixel and 1st element stores the y pixel
# NOTE: DO NOT change the value of this "setpoint" list
setpoint = [0, 0]

# Global tuple to store the start and end cell coordinates of the maze
# The 0th element stores the row and 1st element stores the column
# NOTE: DO NOT change the value of these tuples
start_coord = (0,4)
end_coord = (9,5)

# You can add your global variables here
##############################################################



##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def calculate_path_from_maze_image(img_file_path):
	"""
	Purpose:
	---
	This function reads the image from `img_file_path` input, applies
	Perspective Transform and computes the encoded maze array by calling
	applyPerspectiveTransform and detectMaze functions from task_1b.py.

	It then calls the find_path function from task_4a.py to compute the path
	between start and end coordinate values declared globally.

	Input Arguments:
	---
	`img_file_path` :  [ str ]
		File path of maze image.
	
	Returns:
	---
	`maze_array` 	:   [ nested list of lists ]
		encoded maze in the form of a 2D array
	
	`path` :  [ list of tuples ]
		path between start and end coordinates

	Example call:
	---
	maze_array, path = calculate_path_from_maze_image(img_file_path)
	
	"""

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

						try:
							path = task_4a.find_path(maze_array, start_coord, end_coord)

							if (type(path) is list):

								print('\nPath calculated between %s and %s is = %s' % (start_coord, end_coord, path))
								print('\n============================================')
							
							else:
								print('It seems that path is of type ', type(path),'.\n Make sure that is a list.')
						
						except Exception:
							print('\n[ERROR] Your find_path function in \'task_4a.py\' throwed an Exception, kindly debug your code!')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()

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

	return maze_array, path


def send_data_to_draw_path(rec_client_id, path):
	"""
	Purpose:
	---
	This function should:
	1. Convert and 
	2. Send a flattened path to LUA's drawPath() function.
	
	Teams are free to choose logic for this conversion.

	We have provided an example code for the above.

	Suppose [(1, 5), (2, 5)] is the path given as input to this function. 
	To visualize this path, it needs to be converted to CoppeliaSim coordinates.

	The following points should be considered:

	1. The entire maze is 1m x 1m in CoppeliaSim coordinates. Dividing this by 10 rows and 
	10 columns, we get the size of each cell to be 10cm x 10cm.

	2. The x axis of CoppeliaSim corresponds to the row and y axis corresponds to the column.

	3. The x and y origin of CoppeliaSim coincides with the center of 4th and 5th row as well
	as column. When row and column are both 0, the corresponding CoppeliaSim coordinates are
	(-0.5,-0.5). Since we need the path from the center of the cell, an offset of 45cm is required.
	
						0.45m								0.5m
		 |←-----------------------------→|←----------------------------------→|
		 |								 |									  |
	 0	 |	 1		 2		 3		 4	 |	 5		 6 		 7		 8		 9|
	 _	 |	 _	 	 _	 	 _	 	 _	 |	 _	 	 _	 	 _	 	 _	 	 _|_ _ _ _ _ _ _ 
	|_|  |  |_|		|_| 	|_| 	|_|  |	|_| 	|_| 	|_| 	|_| 	|_|		0		↑
		 |	 							 |													|
	 _	 	 _	 	 _	 	 _	 	 _	 |	 _	 	 _	 	 _	 	 _	 	 _				|
	|_| 	|_|		|_| 	|_| 	|_|  |	|_| 	|_| 	|_| 	|_| 	|_|		1		|
										 |													|
	 _	 	 _	 	 _	 	 _	 	 _	 |	 _	 	 _	 	 _	 	 _	 	 _				|
	|_| 	|_|		|_| 	|_| 	|_|  |	|_| 	|_| 	|_| 	|_| 	|_|		2		|0.5m
										 |													|
	 _	 	 _	 	 _	 	 _	 	 _	 |	 _	 	 _	 	 _	 	 _	 	 _				|
	|_| 	|_|		|_| 	|_| 	|_|  |	|_| 	|_| 	|_| 	|_| 	|_|		3		|
										 |													|
	 _	 	 _	 	 _	 	 _	 	 _	 |	 _	 	 _	 	 _	 	 _	 	 _				|
	|_| 	|_|		|_| 	|_| 	|_|  |	|_| 	|_| 	|_| 	|_| 	|_|		4		|
									   (0,0) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _↓
	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _
	|_| 	|_|		|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_|		5

	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _
	|_| 	|_|		|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_|		6

	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _
	|_| 	|_|		|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_|		7

	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _
	|_| 	|_|		|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_|		8

	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _	 	 _
	|_| 	|_|		|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_| 	|_|		9
	|		|
	| 0.1m	|
	|←-----→|


	Using the above information we map the cell coordinates to the CoppeliaSim coordinates.
	The formula comes out to be:

	CoppeliaSim_coordinate=(((10*row_or_column_number) - 45)/100) m

	Hence the CoppeliaSim coordinates for the above example will be:

	coppelia_sim_coord_path = [-0.35, 0.05, -0.25, 0.05]

	Here we are sending a simple list with alternate x and y coordinates.

	NOTE: You are ALLOWED to change this function according to your logic.
		  Visualization of this path in the scene is MANDATORY.
	
	Input Arguments:
	---
	`rec_client_id` 	:  [ integer ]
		the client_id generated from start connection remote API, should be stored in a global variable

	`path` 	:  [ list ]
		Path returned from task_4a.find_path() function.
	
	Returns:
	---
	None
	
	Example call:
	---
	send_data_to_draw_path(rec_client_id,path)
	
	"""
	global client_id
	client_id = rec_client_id

	##############	IF REQUIRED, CHANGE THE CODE FROM HERE	##############

	coppelia_sim_coord_path = []
	
	for coord in path:
		for element in coord:
			coppelia_sim_coord_path.append(((10*element) - 45)/100)
	
	print('\n============================================')
	print('\nPath sent to drawPath function of Lua script is \n')
	print(coppelia_sim_coord_path)

	inputBuffer = bytearray()

	return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id, \
						'top_plate_respondable_1', sim.sim_scripttype_customizationscript, 'drawPath', [], \
						coppelia_sim_coord_path, [], inputBuffer, sim.simx_opmode_blocking)
	
	##################################################


def convert_path_to_pixels(path):
	"""
	Purpose:
	---
	This function should convert the obtained path (list of tuples) to pixels.
	Teams are free to choose the number of points and logic for this conversion.

	Input Arguments:
	---
	`path` 	:  [ list ]
		Path returned from task_4a.find_path() function.
	
	Returns:
	---
	`pixel_path` : [ type can be decided by teams ]

	Example call:
	---
	pixel_path = convert_path_to_pixels(path)
	
	"""
	##############	ADD YOUR CODE HERE	##############


	
	##################################################	
	return pixel_path


def traverse_path(pixel_path):

	"""
	Purpose:
	---
	This function should make the ball traverse the calculated path.
	
	Teams are free to choose logic for this function.

	NOTE: Refer the code of main function in task_3.py.

	Input Arguments:
	---
	`pixel_path` : [ type can be decided by teams ]
	
	Returns:
	---
	None
	
	Example call:
	---
	traverse_path(pixel_path)

	"""
	##############	ADD YOUR CODE HERE	##############



	##################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function does the following:
# 						- imports 'task_1b' file as module
# 						- imports 'task_1a_part1' file as module
#						- imports 'task_2a' file as module
#						- imports 'task_2b' file as module
#						- imports 'task_3' file as module
#						- imports 'task_4a' file as module
# 						- takes 'maze00.jpg' image file as input
# 						- calls calculate_path_from_maze_image() function 
# 						- calls init_remote_api_server() function in 'task_2a' to connect with CoppeliaSim Remote API server
#						- then calls send_data() function in 'task_2b' to send maze array data to LUA script
# 						- then calls start_simulation() function in 'task_2a' to start the simulation
#						- then calls init_setup() in 'task_3' function to store the required handles in respective global variables and complete initializations if required
#						- then calls send_data_to_draw_path() function to draw the calculated path in LUA script
#						- then calls convert_path_to_pixels() function to get the path in terms of pixels so that it can be fed as setpoint to the control logic
#						- then calls traverse_path() function to make the ball follow the path calculated
# 						- then calls stop_simulation() function in 'task_2a' to stop the current simulation
#						- then calls exit_remote_api_server() function in 'task_2a' to disconnect from the server

# NOTE: Write your solution ONLY in the space provided in the above functions. Main function should NOT be edited.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')
	
	if os.path.exists(img_file_path):
		
		try:
			maze_array,path = calculate_path_from_maze_image(img_file_path)
		
		except Exception:
			print('\n[ERROR] Your calculate_path_from_maze_image() function throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()
	else:
		print('\n[ERROR] maze0' + str(file_num) + '.jpg not found. Make sure "test_cases" folder is present in current directory.')
		print('Your current directory is: ', os.getcwd())
		sys.exit()

	# Initiate the Remote API connection with CoppeliaSim server
	print('\nConnection to CoppeliaSim Remote API Server initiated.')
	print('Trying to connect to Remote API Server...')

	try:
		client_id = task_2a.init_remote_api_server()

		if (client_id != -1):
			print('\nConnected successfully to Remote API Server in CoppeliaSim!')

			try:
				# Send maze array data to CoppeliaSim via Remote API
				return_code = task_2b.send_data(client_id,maze_array)

				if (return_code == sim.simx_return_ok):
					# Starting the Simulation
					try:
						return_code = task_2a.start_simulation()

						if (return_code == sim.simx_return_novalue_flag):
							print('\nSimulation started correctly in CoppeliaSim.')
							
							# Storing the required handles in respective global variables.
							try:
								task_3.init_setup(client_id)
								try:
									send_data_to_draw_path(client_id,path)
								
								except Exception:
									print('\n[ERROR] Your send_data_to_draw_path() function throwed an Exception. Kindly debug your code!')
									print('Stop the CoppeliaSim simulation manually.\n')
									traceback.print_exc(file=sys.stdout)
									print()
									sys.exit()
							
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
					print('\n[ERROR] Failed sending data to CoppeliaSim!')
					print('send_data function in task_2b.py is not configured correctly, check the code!')
					print()
					sys.exit()

			except Exception:
				print('\n[ERROR] Your send_data function throwed an Exception, kindly debug your code!')
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

	try:
		pixel_path = convert_path_to_pixels(path)
		print('\nPath calculated between %s and %s in pixels is = %s' % (start_coord, end_coord, pixel_path))
		print('\n============================================')

		try:
			traverse_path(pixel_path)
		
		except Exception:
			print('\n[ERROR] Your traverse_path() function throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()
	
	except Exception:
		print('\n[ERROR] Your convert_path_to_pixels() function throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
	
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
