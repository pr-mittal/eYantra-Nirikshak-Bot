#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SLICE_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            SLICE_PY.py
*  Created:             04/10/2020
*  Last Modified:       04/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
 
    # Write your code from here
    #taking input
    for i in range(test_cases):
        n=int(input());
        list=input().split()
        print(list)
        # for j in range(n):
        #     list[j]=int(list[j])
        #printing output
        # print(list[-1::-1])
        
 


# In[9]:


#list=['-2', '3', '-5', '1', '8', '-4', '2', '7']
#rint(list[-1::-1])
#l2=list[-1::-1]
#print(l2)
print(" ".join(list[-1::-1]))
# print(map(lambda x: x+3,list[0::3]))
print(" ".join(map(lambda x: str(int(x)+3),list[3::3])))
# print(map(lambda x: x-7,list[0::3]))
print(" ".join(map(lambda x: str(int(x)-7),list[5::5])))
#reduce
sum=0
for i in list[3:8]:
    sum=int(i)+sum
print(sum)

