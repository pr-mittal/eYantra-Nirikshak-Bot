import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)
_,frame=cap.read()
mask=np.zeros(frame.shape[:2],np.uint8)

bgmodel=np.zeros((1,65),np.float64)
fgmodel=np.zeros((1,65),np.float64)

rect=(int(frame.shape[0]/10),int(frame.shape[0]/10),int(frame.shape[0]*9/10),int(frame.shape[0]*9/10))
cv2.grabCut(frame,mask,rect,bgmodel,fgmodel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==0)|(mask==2),0,1).astype('uint8')
#(mask==0)|(mask==2), i.e. if background give it the value 0 else 1
img=frame*mask2[:,:,np.newaxis]
#np.newaxis is used for broadcasting
plt.imshow(img)
plt.colorbar()
plt.show()

cv2.destroyAllWindows()
cap.release()

