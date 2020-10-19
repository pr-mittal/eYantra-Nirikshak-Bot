import cv2
import numpy as np
#default 1st cam is 0
cap=cv2.VideoCapture(0)
#if we want to take a video input
#cap=cv2.VideoCapture('<name>')
#loop for taking frames from the video and analyzing it
while True:
    #this takes one frame if it reads the fame then saves it in frame otherwise returns
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    #breakinf the loop
    #cv2.waitKey(0) means press any key and program ends
    #            1        it ends automatically
    #0xFF is hexadecimal binary for 11111111 is used in bitwise 'and' opeator to get the last 8 bits
    #as soon as input is done cv2.waitKey(0 or 1) with 0xFF(11111111) gives 8 bit binary valu of key if it is binary('q') then we move forward
    #ord() gives ascii unicode of the string 'q'
    '''
    waitKey(0) will pause your screen because it will wait infinitely for keyPress on your keyboard and will not refresh the frame( cap. read() ) using your WebCam.
    waitKey(1) will wait for keyPress for just 1 millisecond and it will continue to refresh and read frame from your webcam using cap.
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#impotant to end all running processes
cap.release()
cv2.destroyAllWindows()
