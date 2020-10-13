#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code D2BIN_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			D2BIN_PY.py
*  Created:				04/10/2020
*  Last Modified:		04/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Function to calculate Euclidean distance between two points
def dec_to_binary(n):

    bin_num =""
    i=n
    # Complete this function to return binary equivalent output of the given number 'n' in 8-bit format
    while(i>0):
        bin_num=str(i%2)+bin_num
        i=i//2
    bin_num="0"*(8-len(bin_num))+bin_num
    return bin_num


# Main function
if __name__ == '__main__':

    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the n value
    for case in range(1,test_cases+1):
        # take the n input values
        n = int(input())
        
        # print (n)
        
        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        bin_num = dec_to_binary(n)
        print(bin_num)

