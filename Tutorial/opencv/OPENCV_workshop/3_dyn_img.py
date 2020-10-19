import cv2
cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	cv2.imshow('frame', frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


