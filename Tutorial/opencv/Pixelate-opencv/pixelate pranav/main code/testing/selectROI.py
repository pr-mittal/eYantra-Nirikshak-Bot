import cv2
import numpy as np

img=cv2.imread('tacarena.jpg')
r=cv2.selectROI(img)
#print(r)
img_hsr=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#r=y,h,x,w
roi=img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
#print(roi.shape)
roi_hsr=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
maxh=0
maxs=0
maxv=0
minh=180
mins=255
minv=255
for pixel in roi_hsr:
    #print(pixel)
    for l in pixel:
        #print(l)
        if((maxh<=l[0])):
            maxh=l[0]
        if((maxs<=l[1])):
            maxs=l[1]
        if((maxv<=l[2])):
            maxv=l[2]
        if((minh>=l[0])):
            minh=l[0]
        if((mins>=l[1])):
            mins=l[1]
        if((minv>=l[2])):
            minv=l[2]
        
min_threshold=np.array([minh,mins,minv],dtype=np.int32)
print(min_threshold)
max_threshold=np.array([maxh,maxs,maxv],dtype=np.int32)
print(max_threshold)
