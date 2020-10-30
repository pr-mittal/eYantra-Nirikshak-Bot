import cv2
import numpy as np

img=cv2.imread('pcrop.jpg',-1)
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
minh=0
mins=0
minv=0
for pixel in roi_hsr:
    #print(pixel)
    for l in pixel:
        #print(l)
        if(maxh<=l[0]):
            maxh=l[0]
        if(maxs<=l[1]):
            maxs=l[1]
        if(maxv<=l[2]):
            maxv=l[2]
        if(minh>=l[0]):
            minh=l[0]
        
min_threshold=np.array([minh,40,0],dtype=np.int32)
print(min_threshold)
max_threshold=np.array([maxh,maxs,maxv],dtype=np.int32)
print(max_threshold)
mask=cv2.inRange(img_hsr,min_threshold,max_threshold)

#morphological transformation
'''kernel1=np.ones((2,2),dtype=np.int8)
mask=cv2.erode(mask,kernel1)

kernel2=np.ones((2,2),dtype=np.int8)
mask=cv2.dilate(mask,kerne2)
'''
cv2.imshow('mask',mask)
contours_mask,_=cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours_mask:
    area=cv2.contourArea(cnt)
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if(len(approx)==3):
        if area>50:
            M = cv2.moments(approx)
            if M["m00"] !=0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                centroid=[cX,cY]
                print('centroid of triangle is',centroid)



