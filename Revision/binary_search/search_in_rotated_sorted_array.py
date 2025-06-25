def sorted_arr(arr,target):

    s,e = 0, len(arr)-1

    while  s <= e :
        mid = (s+e)//2
        if target ==arr[ mid ]:
            return mid

        elif target >arr[mid] or target < arr[s]:
            s = mid+1

        
        else : e = mid-1
    return -1


arr = [5,1,3]
target = 5
print(sorted_arr(arr,target))