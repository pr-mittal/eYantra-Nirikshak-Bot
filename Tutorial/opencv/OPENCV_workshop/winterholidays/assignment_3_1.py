import cv2
import numpy as np
import serial

ser=serial.Serial('',9600)
#Insert port name under the quotes

color=[[[0,0,83],[80,130,255]],[[135,0,0],[255,200,134]],[[0,168,0],[150,255,190]]]
#Here we will define the color ranges of red Blue and Green Colors in this order


image=['./opencv1.jpeg','./opencv2.png']
#Here we store image names. Ensure you save the images in the same directory of this solution.py file


ans=['red','blue','green']
#For writing new image names


enc=['r','b','g']
#For Seial Communication
"""
   You can do the task either taking the image in BGR format(by default) or in 
   HSV format. You just need to adjust the values. Here I have written the code
   for BGR format
"""
for j in range(0,2):
    img=cv2.imread(image[j]) #Reading the 2 images
    for i in range(0,3):
        #Doing the tasks for Red Blue and Green
        lower=np.array(color[i][0])
        upper=np.array(color[i][1])
        mask=cv2.inRange(img,lower,upper)  #Masking
        cv2.imshow(mask,'aa');
        cv2.waitKey(0);
        res=cv2.bitwise_and(img,img,mask=mask)
        res[np.where((res==[0,0,0]).all(axis=2))] = [255,255,255]
        #np.where searches for a given value in the entire matrix and replaces with whatever value you wish
        #Don't forget to give the extension
        cv2.imwrite(ans[i]+str(j+1)+'.jpg',res)

        ser.write(b(enc[i]))
        """
        For Serial Communication.
        Here I have done simultaneously for the images, i.e. 
        first all 3 LED's light up one by one for each image, after 
        that I will light up all the LED.However, if you have detected 
        a color in both the images at once and after that light the LED
        it is also correct
        """ 
    ser.write(b'a')
    ser.close()