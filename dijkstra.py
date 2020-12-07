#!/usr/bin/env python
# coding: utf-8

# In[64]:


import numpy as np


# In[85]:


def visitAdjacent(graph,shape,node,distance,parent):
    #Update distance value of all adjacent vertices of u. 
    #For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.
    #print(node)
    #adjacent nodes are top(node-n),right(node+1),bottom(node+n),left(node-1)
    n=shape[1]
    directions=graph[node]
    
    #index out of range error, as matrix might go out of range
    if(directions//8==1):
        #top
        if(distance[node-n]>distance[node]+1):
            distance[node-n]=distance[node]+1
            parent[node-n]=node
            #print("t",end="")
        directions=directions%8
    if(directions//4==1):
        #right
        if(distance[node+1]>distance[node]+1):
            distance[node+1]=distance[node]+1
            parent[node+1]=node
            #print("r",end="")
        directions=directions%4
    if(directions//2==1):
        #bottom
        if(distance[node+n]>distance[node]+1):
            distance[node+n]=distance[node]+1
            parent[node+n]=node
            #print("b",end="")
        directions=directions%2
    if(directions//1==1):
        #left
        if(distance[node-1]>distance[node]+1):
            distance[node-1]=distance[node]+1
            parent[node-1]=node
            #print("l",end="")
    
    return distance,parent
def calcPath(parent,src,dst):
    #print(parent)
    path=[]
    #tracing back the path based on the parent matrix
    while(True):
        path=[dst+1]+path
        #print(dst,end=" ")
        if(src==dst):
            break
        dst=int(parent[dst])
    return path
def findNextNode(distance,finalised):
    #Pick a vertex u which is not there in sptSet and has minimum distance value.
    min=np.inf
    minIndex=-1
    for x in range(len(distance)):
        if x not in finalised:
            #print(distance[x])
            #print(distance[x]<min)
            if(distance[x]<min):
                min=distance[x]
                minIndex=x
            
    return minIndex
def dijkstra(graph,shape,src,dst):
    #we are using a 1 D graph of dimension (m*n)
    #graph=[6, 7, 5, 3, 6, 7, 5, 3,14, 9, 4, 11, 10, 12, 3, 10,10, 6, 5, 11, 10, 6, 9, 8,10, 12, 3, 10, 10, 10, 6, 3,12, 1, 8, 12, 9, 12, 5, 9]
    distance=np.ones(len(graph)) * np.inf
    #print(np.ones(len(graph)) * np.inf)
    parent=np.ones(len(graph)) * np.inf
    finalised=[]# whose minimum distance from source is calculated and finalized. 
    path=[]
    #print(distance)
    
    #starting node
    src=src-1
    dst=dst-1
    distance[src]=0
    #i=0
    while(True):
        #print(i)
        #i=i+1
        #Pick a vertex u which is not there in sptSet and has minimum distance value.
        #print(distance,finalised)
        minpos=findNextNode(distance,finalised)
        #if destination is reached break the loop
        if(minpos==dst):
            break
        #ERROR
        if(minpos==-1):
            print("ERROR in calculating findNextNode(distance,finalised)")
            break
        #visit the adjacent nodes and continue again
        distance,parent=visitAdjacent(graph,shape,minpos,distance,parent)
        #Include u to sptSet.
        finalised+=[minpos]
        #print(minpos,end=" ")
        
    #print(parent)
    path=calcPath(parent,src,dst)
    #print(path)
    return path
# dijkstra([],[5,8],1,40)


# In[ ]:


if __name__ == "__main__":
    m,n=input().split(" ")
    m=int(m)
    n=int(n)
    graph=[]
    for x in range(m):
        row=[]
        for y in range(n):
            num,t,r,b,l=input().split(" ")
            t=int(t)
            r=int(r)
            b=int(b)
            l=int(l)
            row+=[t*8+r*4+b*2+l*1]
            #print(m*x+y,end=" ")
        graph+=row
    #print(graph)
    path=dijkstra(graph,[m,n],1,m*n)
    for i in path:
        print(i,end=" ")

