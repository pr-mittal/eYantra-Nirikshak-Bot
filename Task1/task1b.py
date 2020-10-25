import numpy as np
import cv2
#capture video
cap = cv2.VideoCapture("ballmotionwhite.m4v")
#cap.set(3,500)    ##setting for width(3) 
#cap.set(4,500)    ##setting for height(4) 
#cap.set(10,100)   ##setting for brightness
l1 = np.array([0,50,50])
u1 = np.array([10,255,255])
l2 = np.array([170,50,50])
u2 = np.array([180,255,255])
kernel = np.ones((5,5),np.uint8)
if (cap.isOpened()== False):
    print("Error opening video stream or file")
frame_n =0
while (cap.isOpened()):
    # Capture frame-by-frame
    # ret = if the frame is collected or not (boolean),frame = part of video as a frame
    ret, img = cap.read()
    frame_n = frame_n +1
    img =cv2.resize(img,(960,540))
    # Display the resulting frame
    #cv2.imshow('Frame', frame)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #imgStack = stackImages(0.5,[imgGray,imgCanny])
    #lower = np.array([17, 15, 100],dtype = "uint8")
    #upper = np.array([50, 56, 200],dtype="uint8")
    #mask = cv2.inRange(img, lower, upper)
    
    m1 = cv2.inRange(imgHsv,l1,u1)
    m2 = cv2.inRange(imgHsv,l2,u2)
    m3 = m1+m2
    m3 = cv2.erode(m3,kernel,iterations =6)
    m3 = cv2.dilate(m3,kernel,iterations = 6)
    output = cv2.bitwise_and(imgHsv, imgHsv, mask = m3)
    #working with a single contour
    _ , contours, heirarchy = cv2.findContours(m3,1,2)
    #print(len(contours)) only one contour is there
    M = cv2.moments(contours[0])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print(f"/",frame_n,"--",cX*2,",",cY*2)
    cv2.imshow('Frame', m3)
    
    
  # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 # When everything done, release the video capture object(inportant)
cap.release()
 # Closes all the frames
cv2.destroyAllWindows()