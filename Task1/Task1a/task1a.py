#tyhis is working fine final########################################################################
import cv2
import numpy as np
 #------------------------------------------------------------------------------------------------------
#stacking function(do not read this)
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
#-----------------------------------------------------------------------------------------------------
#function to get contours
def getContours(img):
    _ , contours, heirarchy = cv2.findContours(img,1,2)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #using moments
        M = cv2.moments(cnt)
        #contour on image--#img   #countour #index #color #thickness
        if area>500 and area<(img.shape[0]*img.shape[1]-100000): #to avoid the noise in the image
            print(f"area =",area) #print area
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)#index =-1 means all the countours
            perimeter = cv2.arcLength(cnt,True) #it gives the perimeter of each shape(true is for closed shape)
            aprox = cv2.approxPolyDP(cnt,0.02*perimeter,True) #this will give coridinates of all the corner points
            print(f"Corners =",len(aprox)) #this will print number of corneres in each cotour
            n_corners = len(aprox)
            #now we will draw a rounded box around the detected object(or shape)
            x, y, w, h = cv2.boundingRect(aprox) #this function takes the corners cordinates of shape and returns the x,y,width,hight of the bounding box(x,y are top left corner cordinate)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),5) #draw a bounding rect with the corinates we got (x,y)=tope left,(x+w,y+h)=right bottom corner
            
            #=============================================================================================
            #for detection of shape
            obj = "Circle"
            if n_corners ==3:
                obj = "Triangle"    
            if n_corners ==5:
                obj = "Pentagon"
            if n_corners ==6:
                obj = "Hexagon"
            if n_corners ==4:
                obj = "4sideNOSq "
                ratio = float(w/h)
                if ratio > 0.95 and ratio < 1.05:
                    obj = "Square"
                #=================================shape 4 corners trial===============================
                topLeft = imgT[y+3,x+3]
                topRight = imgT[y+3,x+w-3]
                btmLeft = imgT[y+h-3,x+3]
                btmRight = imgT[y+h-3,x+w-3]
                #print(imgT[y+3,x+3])
                #print(imgT[y+3,x+w-3])
                #print(imgT[y+h-3,x+3])
                #print(imgT[y+h-3,x+w-3])
                cv2.circle(imgContour, (x+3,y+3), 7, (0,0,0), -1)
                #cv2.circle(imgContour, (cX, cY), 7, (255, 255, 255), -1)
                #cv2.circle(imgContour, (cX, cY), 7, (255, 255, 255), -1)
                #cv2.circle(imgContour, (cX, cY), 7, (255, 255, 255), -1)
                k = topLeft==imgT[cY,cX]
                l = topRight==np.array([b,g,r])
                m = btmLeft==np.array([b,g,r])
                p = btmLeft==np.array([b,g,r])
                print(topLeft)
                print(f"-",k," ",l," ",m," ",p)
                kp = k.all()
                lp = l.all()
                mp = m.all()
                pp = p.all()
                if (ratio < 0.97 or ratio > 1.03) and kp and lp and mp and pp:
                    obj = "Rectangle"
                #=================================shape 4 corners trial===============================
                
            print(f"shape =",obj) #print shape
            cv2.putText(imgContour,obj,(x+(w//2)-60,y+(h//2)-5),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,0,0),2)
            #===========================================================================================
            ##for centroid
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            print(f"centroid = ",(cX,cY)) #print centroid
            cv2.circle(imgContour, (cX, cY), 7, (255, 255, 255), -1)
            #print(imgT[cY,cX])
            ##color detection
            r = imgT[cY,cX][2]
            g = imgT[cY,cX][1]
            b = imgT[cY,cX][0]
            if r<=255 and r>245 :
                color ="Red"
            elif g<=150 and g>120 :
                color ="Green"
            elif b<=255 and b>245 :
                color ="Blue"
            else:
                color ="Unknown"
            print(imgT[cY,cX])
            print(color)
            print("==================================")
        ##till now it will draw all the contours in the image
            #print(imgT[cX][cY])
#-----------------------------------------------------------------------------------------------------
#Starting function
import cv2
import numpy as np

img = cv2.imread('Test3.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

ret,thresh1 = cv2.threshold(imgGray,120,255,cv2.THRESH_BINARY)

imgContour = img.copy()
imgT = img.copy()
imgBlank = np.zeros_like(img) #zeroes matrix of shape as same as img
#cv.imshow("Gray",imgGray)
#cv.imshow("ORIGINAL",img)
#cv.imshow("blur",imgBlur)
getContours(thresh1)
imgStack = stackImages(0.3,([img,thresh1,thresh1],[imgGray,imgContour,imgT]))
#v2.imshow("stack",imgStack)
#cv2.imshow("stack",thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------------------------------------------------------------------------
#some theory

#For better accuracy, use binary images. 
#So before finding contours, apply threshold or canny edge detection.
#In OpenCV, finding contours is like finding white object from black background. 
#So remember, object to be found should be white and background should be black.
#---------
##If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored.
#But actually do we need all the points? For eg, you found the contour of a straight line. 
#Do you need all the points on the line to represent that line? 
#No, we need just two end points of that line. This is what cv2.CHAIN_APPROX_SIMPLE does.
#It removes all redundant points and compresses the contour, thereby saving memory.
#--------
#final -------------------------------
