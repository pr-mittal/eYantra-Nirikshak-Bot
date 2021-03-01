# def customizePixelPath(pixel_path):
# 	copy=[[pixel_path[0][0],pixel_path[0][1],0]]
# 	ratio=[5,1]
# 	for i in range(1,len(pixel_path)-1):
# 		copy.append([pixel_path[i][0],pixel_path[i][1],0])
# 		coord=[-1,-1,1]
# 		#getting an extra setpoint before destination
# 		coord[0]=(ratio[0]*pixel_path[i+1][0]+ratio[1]*pixel_path[i][0])/(ratio[0]+ratio[1])
# 		coord[1]=(ratio[0]*pixel_path[i+1][1]+ratio[1]*pixel_path[i][1])/(ratio[0]+ratio[1])
# 		copy.append(coord)
# 	# copy.append([pixel_path[len(pixel_path)-2][0],pixel_path[len(pixel_path)-2][1],0])
# 	copy.append([pixel_path[len(pixel_path)-1][0],pixel_path[len(pixel_path)-1][1],0])
# 	print(copy)
#     #in starting check if it is closer to first point or secnd point , if second then simply pass
# 	# if((((pixel_path[i+1][0]-pixel_path[i][0])**2+(pixel_path[i+1][1]-pixel_path[i][1])**2)<128*128) or (pixel_path[i+1][2]==0)):
# 	# 	#normal kp ,ki,kd
# 	# 	pass
# 	# else:
# 	# 	#fast kp,ki,kd
# 	# 	pass
# 	return copy
# def shortenPath(path):
#     #storing the previous index
# 	prev_x=-1
# 	#count the number of x that have had the same value as x, till present existing in the path
# 	#if count=1 and x==prev_x,meaning now 3 consecutive times x has been same
# 	#we delete the prev_node , so the cnt stays 1
# 	cnt_x=0#number of x that have been common
# 	prev_y=-1
# 	cnt_y=0
# 	#print(prev_x,prev_y)
# 	n=len(path)
# 	i=0
# 	while(i<n):

# 		x=path[i][0]
# 		y=path[i][1]
# 		#see if there are coordinates such that x are same in continuation
# 		if(x==prev_x):
# 			if(cnt_x==1):
# 				#remove the coodrdinate before
# 				#as this coordinate(x,y) and (prev_prev_x,prev_prev_y) are sufficient for this line
# 				#print((prev_x,prev_y))
# 				#print("deleted ",prev_x," ",prev_y)
# 				path.remove([prev_x,prev_y])
# 				i-=1#we dont want ncrement in i so to neutralise i+=1 in future
# 			else:
# 				cnt_x=1#if x is same and xnt_x==0, cnt_x=1 , for next time
# 		else:
# 			cnt_x=0#if x are not same
			
# 		#see if there are coordinates such that y are same in continuation
# 		#for documentation see x above
# 		if(y==prev_y):
# 			if(cnt_y==1):
# 				#more 
# 				#remove the coodrdinate before
# 				#print("deleted ",prev_x," ",prev_y)
# 				path.remove([prev_x,prev_y])
# 				i-=1
# 			else:
# 				cnt_y=1
			
# 		else:
# 			cnt_y=0
# 		#storing the previous coordinates
# 		prev_x=x
# 		prev_y=y
# 		i+=1#moving to the next node
# 		n=len(path)#as we keep on deleting the nodes , we need to update the n
# 		#print(x," ",y," ",cnt_x," ",cnt_y)
# 	return path

# # if __name__ =="__main__"
# #uncomment out_coord.append
# pixel_path=[[703.0, 63.0], [704.0, 64.0], [704.0, 192.0], [704.0, 320.0], [576.0, 320.0], [448.0, 320.0], [320.0, 320.0], [320.0, 448.0], [192.0, 448.0], [64.0, 448.0], [64.0, 576.0]]
# pixel_path=getOptimisedPath(pixel_path)
# print(pixel_path)
# customizePixelPath(pixel_path)