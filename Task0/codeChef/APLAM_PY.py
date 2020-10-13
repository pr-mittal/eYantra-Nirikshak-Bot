#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code APLAM_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			APLAM_PY.py
*  Created:				04/10/2020
*  Last Modified:		04/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Import reduce module
from functools import reduce


# Function to calculate Euclidean distance between two points
def generate_AP(a1, d, n):

    AP_series = []

    # Complete this function to return A.P. series
    for i in range(n):
        AP_series.append(a1+i*d)

    return AP_series


# Main function
if __name__ == '__main__':

    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the a1, d and n values
    for i in range(test_cases):
        list=input().split(" ")
        a1=int(list[0])
        d=int(list[1])
        n=int(list[2])
        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series = generate_AP(a1, d, n)
        print(*AP_series)
        #print(AP_series)
        #2 7 12 17 22 27 32
        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series = [x for x in (map(lambda x:x*x,AP_series))]
        print(*sqr_AP_series)
        #print(sqr_AP_series[0])
        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = reduce(lambda x,y:x+y,sqr_AP_series,0)
        #print(AP_series,sqr_AP_series,sum_sqr_AP_series)
        print(sum_sqr_AP_series)


# In[ ]:




