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

# Team ID:			2182
# Author List:		Priyank Sisodia,Pranav Mittal
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					getBorderCoordinates,orderedPolyDp,threshInputImage,drawContours
# Global variables:	
# 					None


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
#import matplotlib.pyplot as plt
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
def orderedPolyDp(corners):
    '''
    Purpose:
    ---
    Return the coordinates in a clockwise order , input can be in random order

    Input Arguments:
    ---
    `corners` :  [ 2D list ]
        [[x1,y1],[x2,y2],[x3,y3],[x4,y4]], take 4 coordinates
    Returns:
    ---
    `rect` :  [2D list]
        [[x1,y1],[x2,y2],[x3,y3],[x4,y4]],orderes in clockwise manner
    Example call:
    ---
    rect=orderedPolyDp(corners)
    '''
    #ordering all the corners(output of aproxpoly give unordered cordinates of shape)

    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum

    s = corners.sum(axis=2)

    rect[0] = corners[np.argmin(s)]
    rect[2] = corners[np.argmax(s)]

    #print(s)
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
    '''
    Purpose:
    ---
    Returns the border coordiantes of table
    Input Arguments:
    ---
    `imgMorph` :  [ np.array ]
        image of table taken by vision sensor resized to 1280 , 1280
    Returns:
    ---
    `rect` :  [ np.array ]
        unorderd coordinated of corners of the table
    Example call:
    ---
    rect=getBorderCoordinates(imgMorph)
    '''
    #maze is an open maze---
    img=imgMorph
    #finding the coordinates of corners of maze border
    #finding the ouutermost square
    contours, heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #############################old code for closed maze#######
    #for c in contours:
    #print(len(contours))
    ##getting the countour having max area
    #row,col=imgMorph.shape
    #maxCnt=contours[0]
    #maxArea=0
    #for cnt in contours:
    #    area=cv2.contourArea(cnt)
    #    if((area>maxArea) and (area<row*col*0.95)):
    #        maxArea=area
    #        maxCnt=cnt
    #perimeter = cv2.arcLength(maxCnt,True)
    #corners = cv2.approxPolyDP(maxCnt, 0.01*perimeter,True)
    ##image = cv2.polylines(img, cnt,True,(255,0,0),5) 
    ##fig.add_subplot(rows,cols,2)
    ##plt.imshow(image)
    ##print(corners)
    #rect=orderedPolyDp(corners)
    #############################code for open maze################
    #calculating bounding rectangles
    contours_poly = []
    boundRect = []
    minArea=100
    row,col=img.shape
    for cnt in contours:
        #image = cv2.polylines(imgCpy, cnt,True,(0,0,255),5)
        perimeter = cv2.arcLength(cnt,True)
        corners = cv2.approxPolyDP(cnt, 0.01*perimeter,True)
        area=cv2.contourArea(cnt)
        #storing coordinates of all contours
        if((area>minArea) and (area<row*col*0.95)):
            #bounding rect for every 
            #[[[ 113   77]] [[  51 2202]] [[2229 2201]] [[2200   79]]]
            #print(corners)
            for corner in corners:
                contours_poly += [corner[0]]
            #boundRect += [cv2.boundingRect(corners)]
    #we have array of all corners and their bounding rect
    #boundRect = np.array(boundRect)
    #print(contours_poly)
    #calculating all coordinates of corners of bounding rect and storing in allvertex
    #x y w h, this is format of bounding rect
    #x y
    #x y+h
    #x+w , y+h
    #x+w y
    #allVertex = list()
    #print(allVertex.shape)
    #for i in range(0,boundRect.shape[0]):
    #    allVertex+=[
    #                 [boundRect[i][0], boundRect[i][1]],
    #                 [boundRect[i][0], boundRect[i][1]+boundRect[i][3]],
    #                 [boundRect[i][0]+boundRect[i][2], boundRect[i][1]+boundRect[i][3]],
    #                 [boundRect[i][0]+boundRect[i][2], boundRect[i][1]]
    #               ]
    #allVertex = np.array(allVertex)
    allVertex=np.array(contours_poly)
    #print(allVertex)
    
    #calculating all corners of maze
    top_left = [0,0]
    top_right = [0,0]
    bottom_left = [0,0]
    bottom_right = [0,0]
    
    #for top_left,sum of coordinates is minimum
    minSum =1e5#as max coord is 1280,1280
    for coord in allVertex:
        sumCordi = coord[0] + coord[1]
        if minSum>sumCordi:
            minSum = sumCordi
            top_left = [coord[0] ,coord[1]]

    #for bottom_right,sum is maximum
    maxSum = 0
    for coord in allVertex:
        sumCordi = coord[0] + coord[1]
        if minSum<sumCordi:
            minSum = sumCordi
            bottom_right = [coord[0], coord[1]]

    #print("topright all")
    #for top_right(diff max-->(x-y))
    maxdiff = 0
    for coord in allVertex:
        diffCordi = coord[0] - coord[1]
        #print(coord[0],coord[1])
        if maxdiff<diffCordi:
            maxdiff = diffCordi
            top_right = [coord[0], coord[1]]

    #for bottom_left(diff max-->(y-x))
    maxdiff = 0
    for coord in allVertex:
        diffCordi = coord[1] - coord[0]
        if maxdiff<diffCordi:
            maxdiff = diffCordi
            bottom_left = [coord[0], coord[1]]

    #=============================================
    #Height = bottom_left[1] - top_left[1]
    #Width = top_right[0] - top_left[0]
    #=======================================================
    rect = np.zeros((4, 2), dtype="float32")
    rect = [[top_left[0],top_left[1]], [top_right[0],top_right[1]], [bottom_right[0],bottom_right[1]], [bottom_left[0],bottom_left[1]]]
    #print(rect)
    #drawContours(img,contours_poly,boundRect,top_right,top_left,bottom_right,bottom_left)
    return np.array(rect, dtype = "float32")
def drawContours(imgCpy,contours_poly,boundRect,top_right,top_left,bottom_right,bottom_left):
    '''
    Purpose:
    ---
    Not used ,made for testing
    Shows the points and cropped image of the table
    Input Arguments:
    ---
    'imgCpy':[np.array]
        Table image from vision sensor
    'contours_poly':[lsist]
        contains list of all contours obtained by cv2.findContours
    'boundRect':[list]
        The table outer coordinates estimated by applyPerspective Transformation
    'top_right':[list]
        [x,y] of top right corner
    'top_left':[list]
        [x,y] of top left corner
    'bottom_right':[list]
        [x,y] of bottom right
    'bottom_left':[list]
        [x,y] of bottom left
    Returns:
    ---
        No returns
    Example call:
    ---
    < Example of how to call this function >
        drawContours(imgCpy,contours_poly,boundRect,top_right,top_left,bottom_right,bottom_left)
    '''
    #drawing = np.zeros((imgCpy.shape[0],imgCpy.shape[1], 3), dtype=np.uint8)
    drawing=imgCpy
    for i in range(len(contours_poly)):
        color = (0,255,0)
        colorp = (0,0,255)
        cv2.drawContours(drawing, contours_poly, i, colorp)
        cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])),(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 10)
        #print(boundRect)
        #boundRect = np.array(boundRect)
        #print(boundRect.shape)
    
    drawing = cv2.circle(drawing, tuple(top_left), 20, (255,0,0), 6) #correct
    drawing = cv2.circle(drawing, tuple(bottom_right), 20, (255,0,0), 6) #correct
    # print("topright and fucking bottom left")
    # print(top_right)
    # print(bottom_left)
    drawing = cv2.circle(drawing, tuple(top_right), 20, (255,0,0), 6)
    drawing = cv2.circle(drawing, tuple(bottom_left), 20, (255,0,0), 6)
    #plt.imshow(cv2.cvtColor(drawing,cv2.COLOR_BGR2RGB))
def threshInputImage(img):
    '''
    Purpose:
    ---
    Apply various image thresholding techniques to increse the quality of image for use

    Input Arguments:
    ---
    `img` :  [ np.array ]
        Colored 1280,1280 image obtained form vision conveyer
    Returns:
    ---
    `imgMorph` :  [ np.array ]
        img obtained after applying threshlding
    Example call:
    ---
    imgMorph=threshInputImage(img)
    '''
    #thresholding image overall by increasing contrast and features
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGray = cv2.GaussianBlur(imgGray,(7,7),1)
    
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    #imgGray = clahe.apply(imgBlur)
    
    #fig=plt.figure(figsize=(8,8))
    #fig.add_subplot(1,2,1)
    #hist, bins = np.histogram(imgGray.ravel(),256,[0,256]) 
    #plt.plot(hist);
    #fig.add_subplot(1,2,2)
    #hist, bins = np.histogram(imgBlur.ravel(),256,[0,256]) 
    #plt.plot(hist);
    #increase contrast and get a suitable threshold value
    #ret,imgThresh = cv2.threshold(imgBlur,100,255,cv2.THRESH_BINARY)
    ret,imgThresh=cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #plt.imshow(cv2.cvtColor(imgThresh,cv2.COLOR_BGR2RGB))
    #fig.add_subplot(1,2,2)
    #Appplying morphological tranformation for better detection of maze and table borders
    kernel = np.ones((5, 5), np.uint8)
    #imgMorph=cv2.erode(imgThresh,kernel,iterations=2)
    #imgBlank = np.zeros_like(img)
    imgCanny = cv2.Canny(imgThresh,80,80)
    #plt.imshow(cv2.cvtColor(imgCanny,cv2.COLOR_BGR2RGB))
    imgMorph=cv2.dilate(imgCanny,kernel,iterations=6)
    
    return imgMorph

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
    
    #taking image-> gray-> canny ->findContour->draw contour on blank image
    img = cv2.resize(input_img, (1280, 1280))
    #imgThresh=threshInputImage(img)
    #imgMorph=imgThresh
    #rows=2
    #cols=2
    #fig=plt.figure(figsize=(8,8))
    #fig.add_subplot(rows,cols,1)
    imgThresh=threshInputImage(img)
    #imgThresh=threshInputImage(img)
    #plt.imshow(cv2.cvtColor(imgThresh,cv2.COLOR_BGR2RGB))
    #plt.imshow(cv2.cvtColor(imgMorph,cv2.COLOR_BGR2RGB))
    rect=getBorderCoordinates(imgThresh)
    
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
        [maxWidth + 5, 0],
        [maxWidth + 5, maxHeight + 5],
        [0, maxHeight + 5]], dtype = "float32")
    #print(dst)
    #print(rect)
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped_img = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
    #array=cv2.cvtColor(warped_img,cv2.COLOR_BGR2GRAY).ravel()
    #print(array)
    #hist=[]
    #for i in range(len(array)):
    #    if(array[i]!=255):
    #        hist+=[array[i]]
    #hist, bins = np.histogram(hist,256,[0,256]) 
    #plt.plot(hist);
    #fig.add_subplot(rows,cols,3)
    #plt.imshow(cv2.cvtColor(warped_img,cv2.COLOR_BGR2RGB))
    warped_img = cv2.resize(warped_img, (1280, 1280))
    ##################################################

    return warped_img
#path="test_cases/ball.jpeg"
#path="test_cases/maze_t1.jpeg"
# path="generated_images/result_maze00.jpg"
#applyPerspectiveTransform(cv2.imread(path))


# In[72]:



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
    
    #applying hough trasformation on image to calculate the dimensions
    #get maze dimensions
    #imgCanny,maze=mazeDimension(warped_img)
    maze=10
    resultBitmap=threshInputImage(warped_img)
    
    #applying dilation for better maze detection 
    kernel = np.ones((10, 10), np.uint8)
    resultBitmap=cv2.dilate(resultBitmap,kernel,iterations=2)
    # plt.imshow(cv2.cvtColor(resultBitmap,cv2.COLOR_BGR2RGB))
    
    h,w=resultBitmap.shape
    #print(w,h)
    #maxe of 10 x 10
    w=(int)(w/maze) #width of one unit
    h=(int)(h/maze) #height of one unit
    wall=255#the pixel value at wall
    
    maze_array = np.zeros((maze,maze),dtype=np.uint8)
    #r=0;c=0
    #roi= resultBitmap[(int)(h*r):(int)(h*(r+1)),(int)(w*(c+1)-w/2):(int)(w*(c+1)+w/2)]
    #print((int)(h*r-h/2),(int)(h*r+h/2))
    #rows=1
    #cols=2
    #fig=plt.figure(figsize=(8,8))
    #fig.add_subplot(rows,cols,1)
    #plt.imshow(cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    #fig.add_subplot(rows,cols,2)
    #plt.imshow(cv2.cvtColor(resultBitmap,cv2.COLOR_BGR2RGB))
    for r in range(0,maze,1):#row
        for c in range(0,maze,1):#col
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
            #resultBitmap[h*r+1,(int)(w*c+w/2)]=0       #point at center of top
            #resultBitmap[(int)(h*r+h/2),w*(c+1)-1]=0#point at center of right
            #resultBitmap[h*(r+1)-1,(int)(w*c+w/2)]=0   #point at center of bottom
            #resultBitmap[(int)(h*r+h/2),w*c+1]=0       #point at center of left
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
    ##################################################
    maze_array=maze_array.tolist()
    return maze_array
#path="test_cases/maze_t1.jpeg"
#cv2.imread(path)
#detectMaze(applyPerspectiveTransform(cv2.imread(path)))



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



# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION

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



