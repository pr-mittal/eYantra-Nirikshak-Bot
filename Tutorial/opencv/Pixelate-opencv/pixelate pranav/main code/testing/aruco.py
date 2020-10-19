from cv2 import aruco
import cv2
import numpy as np
import math
cap=cv2.VideoCapture(0)
#frame=cv2.imread('aruco.jpg')
aruco_dict=aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters=aruco.DetectorParameters_create()
img=aruco.drawMarker(aruco_dict,76,400)
#cv2.imwrite('aruco.jpg',img)
while True:
    _,frame=cap.read()
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    markerCorners,markerIds,_=aruco.detectMarkers(frame_gray,aruco_dict,parameters=parameters)
    print(markerIds)
    if(markerIds!=None):
        frame_markers=aruco.drawDetectedMarkers(frame.copy(),markerCorners,markerIds)
        cv2.imshow('frame',frame_markers)
        print(markerCorners[0])
    if cv2.waitKey(5) & 0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
