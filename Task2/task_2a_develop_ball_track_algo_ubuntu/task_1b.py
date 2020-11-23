'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:			NB_2182
# Author List:		Priyank Sisodia,Pranav Mittal,Yatharth Bhargava
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					getBorderCoordinates,orderedPolyDp
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################


def orderedPolyDp(corners):
    #ordering all the corners(output of aproxpoly give unordered cordinates of shape)
    rect = np.zeros((4, 2), dtype="float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = corners.sum(axis=2)
    #print(s)
    rect[0] = corners[np.argmin(s)]
    rect[2] = corners[np.argmax(s)]
    #print(rect[0],rect[2])
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(corners, axis=2)
    #print(diff)
    rect[1] = corners[np.argmin(diff)]
    rect[3] = corners[np.argmax(diff)]
    #small fault here ,if diff between both is same ???????????????????
    #order = topleft,topright,bottomright,bottomleft
    #print(f"final cordinates:",rect)
    return rect

def getBorderCoordinates(imgMorph):
    #finding the coordinates of corners of maze border
    #finding the ouutermost square
    contours, heirarchy = cv2.findContours(imgMorph,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #for c in contours:
    #print(len(contours))
    #getting the countour having max area
    maxCnt=contours[0]
    maxArea=0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if(area>maxArea):
            maxArea=area
            maxCnt=cnt
    perimeter = cv2.arcLength(maxCnt,True)
    corners = cv2.approxPolyDP(maxCnt, 0.01*perimeter,True)
    #image = cv2.polylines(img, cnt,True,(255,0,0),5) 
    #fig.add_subplot(rows,cols,2)
    #plt.imshow(image)
    #print(corners)
    return corners
    
##############################################################

def applyPerspectiveTransform(input_img):

    """
    Purpose:
    ---
    takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

    Input Arguments:
    ---
    `input_img` :   [ numpy array ]
        maze image in the form of a numpy array

    Returns:
    ---
    `warped_img` :  [ numpy array ]
        resultant warped maze image after applying Perspective Transform

    Example call:
    ---
    warped_img = applyPerspectiveTransform(input_img)
    """

    warped_img = None

    ##############	ADD YOUR CODE HERE	##############

    ########################################################################
    # Slight modification done in applyPerspectiveTransform(input_img) 
    # No changes in getBorderCoordinates(imgMorph) and orderedPolyDp(corners)
    ########################################################################


    #taking image-> gray-> canny ->findContour->draw contour on blank image
    img = input_img
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    ret,imgThresh = cv2.threshold(imgGray,250,255,cv2.THRESH_BINARY)
    # kernel = np.ones((5, 5), np.uint8)
    #imgMorph=cv2.erode(imgThresh,kernel,iterations=2)
    #imgBlank = np.zeros_like(img)
    imgCanny = cv2.Canny(imgThresh,80,80)
    # Not applying dilate to make the boders sharp only applying 
    # imgMorph=cv2.dilate(imgCanny,kernel,iterations=2)

    corners=getBorderCoordinates(imgCanny)
    rect=orderedPolyDp(corners)
    (tl, tr, br, bl) = rect

    #applying perspective transform
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    # compute the perspective transform matrix and then apply 
    # it on the orignal RGB format image as it is required in 
    # scan_image() function in task_1a_part1.py

    M = cv2.getPerspectiveTransform(rect, dst)
    warped_img = cv2.warpPerspective(img, M, (maxWidth, maxHeight))

    # resizing the image to the required size of (1280, 1280) as given in PS

    warped_img = cv2.resize(warped_img, (1280, 1280))

    ##################################################

    return warped_img


def detectMaze(warped_img):

    """
    Purpose:
    ---
    takes the warped maze image as input and returns the maze encoded in form of a 2D array

    Input Arguments:
    ---
    `warped_img` :    [ numpy array ]
        resultant warped maze image after applying Perspective Transform

    Returns:
    ---
    `maze_array` :    [ nested list of lists ]
        encoded maze in the form of a 2D array

    Example call:
    ---
    maze_array = detectMaze(warped_img)
    """

    maze_array = []

    ##############	ADD YOUR CODE HERE	##############
    
    #plt.imshow(cv2.cvtColor(warped_img,cv2.COLOR_BGR2RGB))
    #print(warped_img)
    #kernel = np.ones((5,5),np.uint8)
    #ret,resultBitmap = cv2.threshold(result,100,255,cv2.THRESH_BINARY)
    #resultBitmap = cv2.erode(resultBitmap,kernel,iterations = 2)#we can change it to 2 if 1 is not working
    #resultBitmap = cv2.resize(resultBitmap,(500,500))
    #resultbgr = cv2.cvtColor(result,cv2.COLOR_GRAY2BGR)
    #resultResize = cv2.resize(resultbgr,(500,500))
    resultBitmap=warped_img.copy()
    h,w=resultBitmap.shape
    #print(w,h)
    #maxe of 10 x 10
    w=(int)(w/10) #width of one unit
    h=(int)(h/10) #height of one unit
    wall=255#the pixel value at wall
    maze=10
    maze_array = np.zeros((maze,maze),dtype=np.uint8)
    for r in range(0,10,1):#row
        for c in range(0,10,1):#col
            score =0
            top = resultBitmap[h*r+1,(int)(w*c+w/2)]==wall       #point at center of top
            right = resultBitmap[(int)(h*r+h/2),w*(c+1)-1]==wall#point at center of right
            bottom = resultBitmap[h*(r+1)-1,(int)(w*c+w/2)]==wall   #point at center of bottom
            left = resultBitmap[(int)(h*r+h/2),w*c+1]==wall         #point at center of left
            #cv.circle(resultResize, (50*m+25,50*(n)), 3, (0,0, 255), -1)
            #cv.circle(resultResize, (50*(m+1)-1,50*(n)+25), 3, (0,0, 255), -1)
            #cv.circle(resultResize, (50*m+25,50*(n+1)-1), 3, (0,0, 255), -1)
            #cv.circle(resultResize, (50*m,50*(n)+25), 3, (0,0, 255), -1)
            #t = tp.all()
            #r = rp.all()
            #b = bp.all()
            #l = lp.all()
            if top :
                score+=2
            if right:
                score+=4
            if bottom:
                score+=8
            if left:
                score+=1
            maze_array[r,c]=score
            resultBitmap[h*r+1,(int)(w*c+w/2)]=0       #point at center of top
            resultBitmap[(int)(h*r+h/2),w*(c+1)-1]=0#point at center of right
            resultBitmap[h*(r+1)-1,(int)(w*c+w/2)]=0   #point at center of bottom
            resultBitmap[(int)(h*r+h/2),w*c+1]=0       #point at center of left
    #print(maze_array)
    #print(resultBitmap.shape)
    #cv2.imshow("hm",resultBitmap)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.imshow("hm",resultbgr)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.circle(resultBitmap, (cX, cY), 7, (255, 0, 0), -1)
    #plt.imshow(cv2.cvtColor(resultBitmap,cv2.COLOR_BGR2RGB))
    #tp = resultBitmap[50*(n),50*m+25]==np.array([0,0,0])
    #rp = resultBitmap[50*(n)+25,50*(m+1)-1]==np.array([0,0,0])
    #bp = resultBitmap[50*(n+1)-1,50*m+25]==np.array([0,0,0])
    #lp = resultBitmap[50*(n)+25,50*m]==np.array([0,0,0])
    #tp = resultBitmap[50*m+25,50*(n)]==np.array([0,0,0])
    #rp = resultBitmap[50*(m+1)-1,50*(n)+25]==np.array([0,0,0])
    #bp = resultBitmap[50*m+25,50*(n+1)-1]==np.array([0,0,0])
    #lp = resultBitmap[50*m,50*(n)+25]==np.array([0,0,0])

    ##################################################
    maze_array=maze_array.tolist()
    return maze_array
#path="test_cases/maze04.jpg"
#cv2.imread(path)
#detectMaze(applyPerspectiveTransform(cv2.imread(path)))


# In[7]:


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# In[ ]:


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv2.imshow('warped_img_0' + str(file_num), warped_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)
            
			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv2.imshow('warped_img_0' + str(file_num), warped_img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

