import numpy as np
import cv2

img=cv2.imread('opencv1.jpeg',cv2.IMREAD_COLOR)
#in open cv it bgr and more the value(0-255) of (blue,green,red)
#example white (255,255,255)
#cv2.line(location to draw,start point,end point,color,line width)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
#cv2.reactangle(location to draw,top right coordinate,bottom right coordinate,color,width)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
#-1 line width is used to fill the predefined images not the polygon
cv2.circle(img,(100,63),55,(0,0,255),-1)
#polygon
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts=pts.reshape((-1,1,2))
#true closes the polygon  i.e. joins last point to first
cv2.polylines(img,[pts],True,(0,255,255),3)
#write test on image
#cv2.putText(img, text, org(where to enter the text) , fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) → None
'''
Parameters:	
img – Image.
text – Text string to be drawn.
org – Bottom-left corner of the text string in the image.
font – CvFont structure initialized using InitFont().
fontFace – Font type. One of FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX, FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_SCRIPT_SIMPLEX, or FONT_HERSHEY_SCRIPT_COMPLEX, where each of the font ID’s can be combined with FONT_ITALIC to get the slanted letters.
fontScale – Font scale factor that is multiplied by the font-specific base size.
color – Text color.
thickness – Thickness of the lines used to draw a text.
lineType – Line type. See the line for details.more examples Type of the line:||8 (or omitted) - 8-connected line(Number of pixels connected together as parts).|| 4 - 4-connected line. ||CV_AA - antialiased line.
bottomLeftOrigin – When true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.
'''

font =cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(0,130),font,5,(200,255,255),2,cv2.LINE_8)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

