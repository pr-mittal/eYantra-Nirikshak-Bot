import cv2


def blackbox(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray', gray)

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	cv2.imshow('hsv', hsv)

	# r = cv2.selectROI(image)
     
    # # Crop image
	# imCrop = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
	# cv2.imshow("imCrop", imCrop)

	return image

image = cv2.imread('1.jpg')
cv2.imshow('image', image)
blackbox(image)
cv2.waitKey(0)