import numpy as np
import cv2
def nothing(x):
    pass
cap=cv2.VideoCapture(1)
cv2.namedWindow('image')
# create trackbars for color change
'''
changed here
'''
cv2.createTrackbar('lowH','image',0,255,nothing)
cv2.createTrackbar('highH','image',255,255,nothing)
 
cv2.createTrackbar('lowS','image',0,255,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)
 
cv2.createTrackbar('lowV','image',0,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)

cv2.createTrackbar('lowth','image',0,255,nothing)
cv2.createTrackbar('highth','image',255,255,nothing)


while True:
    _,frame=cap.read()
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #get current trackbar position
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')
    ilowth=cv2.getTrackbarPos('lowth', 'image')
    ihighth=cv2.getTrackbarPos('highth', 'image')
     # convert color to hsv because it is easy to track colors in this color model
    
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    # Apply the cv2.inrange method to create a mask
    '''
    changed here
    '''
    mask = cv2.inRange(frame, lower_hsv, higher_hsv)
    #theshold to get white box
    _,threshold=cv2.threshold(frame_gray,ilowth,ihighth,cv2.THRESH_BINARY)
    # Apply the mask on the image to extract the original color
    frame = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('final', frame)

    cv2.imshow('threshold',threshold)
    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
