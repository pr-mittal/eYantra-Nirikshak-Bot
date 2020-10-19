def djikstra(current_pos,fianl_pos,input_array,extension=0,min_color=7)
    import numpy as np
    d_arr=np.full((9,9),np.inf)
    v_arr=np.full((9,9),np.inf)
    p_arr=np.full((9,9),np.inf)

    arr=input_array

    for n in range(len(arr)):
        arr[n]=[0]+arr[n]+[0]
    arr=[0,0,0,0,0,0,0,0,0,0,0,0]+arr+[0,0,0,0,0,0,0,0,0,0,0,0]
    
    '''arr=np.array([[0,0,0,0,0,0,0,0,0,0,0],
                  [0,1,2,3,4,3,4,1,3,1,0],
                  [0,1,4,2,2,1,4,3,1,1,0],
                  [0,2,3,1,4,2,1,1,3,2,0],
                  [0,4,1,4,1,0,3,4,1,2,0],
                  [0,1,4,3,0,0,0,2,1,4,0],
                  [0,4,3,4,2,0,1,1,2,3,0],
                  [0,1,1,4,3,1,3,4,2,1,0],
                  [0,4,2,3,1,1,3,1,2,4,0],
                  [0,2,2,1,4,3,3,1,4,2,0],
                  [0,0,0,0,0,0,0,0,0,0,0]])'''

    def dspa(a,b,c,d,e):
        if arr[a+1][b+1]!=0:
            if d_arr[a][b]>c:
                if arr[a+1][b+1]!=min_color:
                    d_arr[a][b]=c+1
                    p_arr[a][b]=d
                    v_arr[a][b]=e+1
                elif arr[a+1][b+1]==min_color:
                    d_arr[a][b]=c
                    p_arr[a][b]=d
                    v_arr[a][b]=e+1
        return arr

    si=current_pos[0]+1
    sj=current_pos[1]+1
    di=final_pos[0]+1
    dj=final_pos[1]+1

    d_arr[si-1][sj-1]=0
    p_arr[si-1][sj-1]=0
    v_arr[si-1][sj-1]=0

    arr1=[[si-1,sj-1]]
    e=0

    def start(si,sj):
        dspa(si+1,sj,d_arr[si][sj],10*(si+1)+sj+1,e)
        dspa(si,sj+1,d_arr[si][sj],10*(si+1)+sj+1,e)
        dspa(si-1,sj,d_arr[si][sj],10*(si+1)+sj+1,e)
        dspa(si,sj-1,d_arr[si][sj],10*(si+1)+sj+1,e)

    while len(arr1)!=0:
        for x in arr1:
            if x[0]!=di or x[1]!=dj:
                start(x[0],x[1])
        e+=1
        arr2=np.where(v_arr==e)
        arr1=list(zip(arr2[0],arr2[1]))
        
    path=[di-1+(dj-1)*9]
    p=p_arr[di-1][dj-1]
    p=int(p)
    p2=(int(p/10)-1+(p%10-1)*9)
    while(p!=0):
        path.append(p2)
        p=p_arr[int(p/10)-1][p%10-1]
        p2=(int(p/10)-1+(int(p%10)-1)*9)
        p=int(p)
        
    path.reverse()
    return(path)
