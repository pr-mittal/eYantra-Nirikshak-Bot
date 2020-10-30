import cv2

image = cv2.imread('1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('window_name', image)
cv2.imshow('GRAY', gray)
cv2.imshow('HSV', hsv)

cv2.waitKey(0)





























# import cv2

# image = cv2.imread('1.jpg')
# cv2.imshow('MyImage', image)
# cv2.waitKey(0)