import cv2
import numpy as np

def change(newVal):
	print('Tracker Has Changed Position!!', newVal)

def draw(frame, x1=15, y1=15, x2=150, y2=150):
	cv2.circle(frame ,(x2, y2) , radius=15, color=(255,0,0), thickness=2)
	cv2.rectangle(frame ,(x1, y1), (x2, y2), color=(0,255,0), thickness=1)
	cv2.arrowedLine(frame, (x1, y1), (x2, y2), color=(255,0,0), thickness=2)
	cv2.line(frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=1)
	cv2.putText(frame, 'text', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.5, color = (255, 255, 0),thickness =  1,lineType =  cv2.LINE_AA)	
	cv2.imshow('frame', frame)

def noiseRemoval():
	msk = np.array([[1,0,1,0],
					[0,1,0,0],
					[0,1,1,1],
					[0,0,0,1],
					[0,0,0,1]], dtype = np.uint8)
	msk*=255
	# Working on Masked Image--------------------------------------
	cv2.imshow('frame', msk)
	kernel = np.ones((3, 3), np.uint8)
	msk1 = cv2.erode(msk, kernel,iterations = 1); cv2.imshow('erode', msk1)
	msk2 = cv2.dilate(msk, kernel,iterations = 1); cv2.imshow('dilate', msk2)
	msk3 = cv2.morphologyEx(msk, cv2.MORPH_OPEN, kernel) #erosion folled by dilution
	msk4 = cv2.morphologyEx(msk, cv2.MORPH_CLOSE, kernel) #dilution folled by erosion
	msk5 = cv2.morphologyEx(msk, cv2.MORPH_GRADIENT, kernel) #It is the difference between dilation and erosion of an image.
	#--------------------------------------------------------------

def imageFilters():
	frame = cv2.imread('1.png')
	gray = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)
	cv2.imshow('frame', frame)

	flipped = cv2.flip(frame, 1) # 0:vertical 1:horizontal -1:both 
	resized = cv2.resize(frame, (340,220));
	cv2.imwrite('savedImg.png', gray)
	copy = np.copy(frame)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY); cv2.imshow('gray', gray)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV); cv2.imshow('hsv', hsv)
	gray2color = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2BGR); cv2.imshow('gray2color', gray2color)

	ret, bin_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY); cv2.imshow('bin_img', bin_img)
	thresholded_gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 
												blockSize = 321, C = 28)

	blurWithEdges = cv2.bilateralFilter(gray, 11, 17, 17); cv2.imshow('blurWithEdges', blurWithEdges)
	edged = cv2.Canny(gray, 30, 200); cv2.imshow('edged', edged)

def imagefilters2():
	cv2.accumulateWeighted(image, bg, aWeight)
	diff = cv2.absdiff(bg.astype("uint8"), image)
	add = cv2.add(img, img2)  # (250)+(250)=>(255)
	add = img+img2  # (250)+(250) => (500-255-1) as pixel starts from 0andNot1
	add = cv2.addWeighted(img, 0.6, img2, 0.4, 0)  # (0.6*img+0.4*img2+0)
	img_or = cv2.bitwise_or(img, img2, mask=msk)
	img_and = cv2.bitwise_and(img, img2, mask=msk)
	msk = cv2.bitwise_not(msk)
	msk = cv2.medianBlur(msk, 7)
	feed = cv2.GaussianBlur(feed,(95,95),0)

	low = np.array([255, 0, 255])
	high = np.array([255, 255, 255])
	mask = cv2.inRange(hsv, low, high)


cv2.namedWindow('frame', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600, 400)
cap = cv2.VideoCapture(0)
cv2.createTrackbar('trackBar', 'frame', 200, 255, change)
val = cv2.getTrackbarPos('trackBar', 'frame')

while True:
	flag, frame = cap.read()
	# draw(frame)
	# noiseRemoval()
	# imageFilters()
	cv2.imshow('frame', frame)

	key = cv2.waitKey(1)
	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
exit()

#--------------------------------------------------------------

cv2.namedWindow('frame', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600, 400)
cv2.moveWindow('feed', x, y)
cv2.destroyWindow('frame')
cv2.createTrackbar('trackBar', 'frame', 200, 255, change)
val = cv2.getTrackbarPos('trackBar', 'frame')

roi = cv2.selectROI(cap.read()[1])
frame = frame[ roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2] ]

#Contours-------------------------------------------------------------
contoursR,hR = cv2.findContours(threshR,1,2)
(cnts, _) = cv2.findContours(thresholded.copy(),
                                    cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(cnt)
x, y, w, h = cv2.boundingRect(cnt)
cv2.drawContours(img, [cnt], -1, (255, 0, 0), 2)
approx = cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt,True), True)
#---------------------------------------------------------------------


#----CREATING VIDEO------------------------------------------------
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640,480))
while True:
	ret, frame = cap.read()
	frame=imchange(frame)
	cv2.imshow('frame', frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break
	elif key == ord('r'):
		out.write(frame)
cap.release()
out.release()
cv2.destroyAllWindows()
#-------------------------------------------------------------------

