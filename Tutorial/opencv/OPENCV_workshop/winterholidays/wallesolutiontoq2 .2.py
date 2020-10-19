#declaration of libraries
import numpy as np
#input of array
'''
#1st attempt
matrix=[]
n=int(input('enter the number of rows and columns:'))
print('enter the array row wise with spaces:')
for i in range(n):
    entries=list(map(int,input().split()))
    np.append(matrix,entries)
np.reshape(matrix,(n,n))
   '''
n=int(input('enter the order of square matrix :'))
matrix=[[0]*n]*n
for i in range(n):
        matrix[i]=list(map(int,input().split()))
print(matrix)
#numpyarray is ready
#calculating sum
#moving along row i.e from column 0 to c-1
moverow=np.sum(matrix,axis=0,dtype='int')
movecol=np.sum(matrix,axis=1,dtype='int')
arr_diagonal=[]
sum1=0
sum2=0
for i in range(n):
    j1=n-1-i
    sum1=sum1+matrix[i][j1]
    j2=i
    sum2=sum2+matrix[i][j2]
arr_diagonal.append(sum1)
arr_diagonal.append(sum2)
'''print(moverow)
print(movecol)
print(arr_diagonal)
'''
#checking sum
check=arr_diagonal[1]
'''check=arr_diagonal[1]
if(arr_moverow!=check):
    print('NO')
else:
    if(arr_movecol!=check):
        print('NO')
    else:
        if(arr_diagonal!=check):
            print('NO')
        else:
            print('YES')
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
'''
flag=0
for i in range(n):
        if(moverow[i]!=check):
            flag=1
for j in range(n):
        if(movecol[j]!=check):
                flag=1
if(arr_diagonal[0]!=check):
        flag=1
if(flag==0):
        print('YES')
else:
        print('NO')
 
#better solution
import numpy as np

n=int(input("Enter number of rows and columns :-"))
arr = np.zeros((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        arr[i,j]=int(input())

print(arr)

#Sum of rows and columns
sum1=np.sum(arr,axis=0)
sum2=np.sum(arr,axis=1)

for i in range(2):
    if sum1[i]!=sum1[i+1] or sum2[i]!=sum2[i+1]:
        print("Not a magic square")
        exit(0)

#Sum of leading diagonal elements
d1=np.trace(arr)

#Flips the array
arr=np.fliplr(arr)
d2=np.trace(arr)

flag1=False
if d1==d2 and d1==sum1[0]:
    flag1=True
  
flag2=np.array_equal(sum1,sum2) #compares two arrays

if flag1==True and flag2==True:
    print("Magic Square ",d1)
else:
    print("Not a magic square")
