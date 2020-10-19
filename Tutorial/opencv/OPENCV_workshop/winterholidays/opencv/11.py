import numpy as np
import cv2

img_bgr=cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

template=cv2.imread('opencv-template-for-matching.jpg',0)
#cv2.imshow('template',template)

#print(template.shape)
'''
Negative values also work to make a copy of the same list in reverse order:

>>> L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
If you have a mutable sequence such as a list or an array you can assign to or delete an extended slice, but there are some differences between assignment to extended and regular slices. Assignment to a regular slice can be used to change the length of the sequence:

>>> a = range(3)
>>> a
[0, 1, 2]
>>> a[1:3] = [4, 5, 6]
>>> a
[0, 4, 5, 6]
Extended slices aren't this flexible. When assigning to an extended slice, the list on the right hand side of the statement must contain the same number of items as the slice it is replacing:

>>> a = range(4)
>>> a
[0, 1, 2, 3]
>>> a[::2]
[0, 2]
>>> a[::2] = [0, -1]
>>> a
[0, 1, -1, 3]
>>> a[::2] = [0,1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: attempt to assign sequence of size 3 to extended slice of size 2
Deletion is more straightforward:

>>> a = range(4)
>>> a
[0, 1, 2, 3]
>>> a[::2]
[0, 2]
>>> del a[::2]
>>> a
[1, 3]
One can also now pass slice objects to the __getitem__ methods of the built-in sequences:

>>> range(10).__getitem__(slice(0, 5, 2))
[0, 2, 4]
Or use slice objects directly in subscripts:

>>> range(10)[slice(0, 5, 2)]
[0, 2, 4]
'''
w,h=template.shape[::-1]

res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.7
#print(res)

loc=np.where(res>threshold)
#print(loc)
#in location y and x coordinates are stored in separate arrays so we zip(*loc[::-1])
#zip basically takes one term from  the two arrays and *loc(* operator) is used to unzip the two terms into p
for p in zip(*loc[::-1]):
    cv2.rectangle(img_bgr,(p[0],p[1]),(p[0]+w,p[1]+h),(0,0,255),2)
cv2.imshow('detected',img_bgr)

