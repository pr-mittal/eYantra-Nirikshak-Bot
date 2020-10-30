import cv2
import numpy as np
import matplotlib.pyplot as plt

#                                   0
img= cv2.imread('opencv1.jpeg',cv2.IMREAD_GRAYSCALE)
#EACH type of colour has a number like grayscale has 0
#IMREAD__COLOR = 1
#IMREAD__UNCHANGED = -1

cv2.imshow('image1',img)
'''
cv2.waitKey(<time>)
'''
'''
Waits for a pressed key.

C++: int waitKey(int delay=0)
Python: cv2.waitKey([delay]) → retval
C: int cvWaitKey(int delay=0 )
Python: cv.WaitKey(delay=0) → int
Parameters:	delay – Delay in milliseconds. 0 is the special value that means “forever”.
The function waitKey waits for a key event infinitely (when \texttt{delay}\leq 0 ) or for delay milliseconds, when it is positive. Since the OS has a minimum time between switching threads, the function will not wait exactly delay ms, it will wait at least delay ms, depending on what else is running on your computer at that time. It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.

Note This function is the only method in HighGUI that can fetch and handle events, so it needs to be called periodically for normal event processing unless HighGUI is used within an environment that takes care of event processing.
Note The function only works if there is at least one HighGUI window created and the window is active. If there are several HighGUI windows, any of them can be active
'''
cv2.waitKey(0)
cv2.destroyAllWindows()

#doing the above job in matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
#cmap->it shows the colours of the matrix in various forms like 'gray' makes the
#image gray and 'jet' makes the image coloured
#interpolation->it is basically 3D effect of the image due to colours
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

cv2.imwrite('wachgray1.png',img)
