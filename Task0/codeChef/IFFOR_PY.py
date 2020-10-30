#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code IFFOR_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			IFFOR_PY.py
*  Created:				19/09/2020
*  Last Modified:		21/09/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Main function
if __name__ == '__main__':
	
	# Take the T (test_cases) input
	test_cases = int(input())
    
	# Write your code from here
	


# In[18]:


for i in range(test_cases):
   n=int(input())
   for j in range(n):
       if(j==n-1):
           if((n-1)%2==0):
               print(2*(n-1),end ="\n")
           else:
               print((n-1)**2,end ="\n")
           break
       if(j==0):
           print(3,end=" ")
       elif(j%2==0):
           print(2*j,end = " ")
       else:
           print(j**2,end = " ")
   
   
       
      

