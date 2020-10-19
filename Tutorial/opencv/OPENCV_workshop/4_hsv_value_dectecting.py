import numpy as np
import cv2
 
def nothing(x):
    pass

 
cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("L - H", "Trackbars", 150, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
 
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
cv2.resizeWindow("HSV", 600, 600)  
cv2.imshow('HSV', cv2.imread('HSV.png'))
 
while True:
    frame = cv2.imread('1.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
 
    lower_blue = np.array([l_h, l_s, l_v]) #init: np.array([100, 100, 100])
    upper_blue = np.array([u_h, u_s, u_v]) #init: np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
 
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Trackbars", result)
 
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break

 
cv2.destroyAllWindows()