#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code DIST_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            DIST_PY.py
*  Created:             02/10/2020
*  Last Modified:       02/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Import any required module/s
import math

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):

    distance = 0
    
    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    print("%.2f"%(distance))
    return distance


# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    for i in range(test_cases):
        # Write the code here to take the x1, y1, x2 and y2 values
        list=input().split(" ")
        x1=int(list[0])
        y1=int(list[1])
        x2=int(list[2])
        y2=int(list[3])
        #print(x1,y1,x2,y2)
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
        compute_distance(x1, y1, x2, y2)

