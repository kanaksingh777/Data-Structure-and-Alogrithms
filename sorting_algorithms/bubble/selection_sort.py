#selection sort - select the max element (or min) from the array , swap it with the last index
#then reduce the array 
def max_1(arr,last_elem):

    max_num=arr[0] 
    for z in range(0,last_elem+1):

        max_num = max(arr[z],max_num)
        
    return arr.index(max_num)
def selection_sort(arr):
    
    for i in range(len(arr)-1):

        last_elem = len(arr)-i-1

        max_elem_idx = max_1(arr,last_elem)

        arr[last_elem],arr[max_elem_idx] = arr[max_elem_idx],arr[last_elem]
    return arr

arr = [4,-1,5,2,0]
print(selection_sort(arr))
    