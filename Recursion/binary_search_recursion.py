def BS(arr,s,e,target):
   
    if s > e :
      return -1 
   
    
    mid = (s+e)//2
    if arr[mid] == target :
        return mid
    
    if arr[ mid] > target :
        return BS(arr,s,mid-1,target)

    if arr[mid] < target :

        return BS(arr,mid+1,e,target)

    


arr = [2,4,5,6,7,24,55]
s = 0
e = len(arr)-1
target =9
ans =BS(arr,s,e,target)
print(ans)