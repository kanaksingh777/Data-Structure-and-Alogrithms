def cycle_sort(arr):

    i = 0 
    while i < len(arr)-1:
        if arr[i] != i+1:
            arr[arr[i]-1] ,arr[i]= arr[i],arr[arr[i]-1]

        else : i +=1 

    return arr



arr = [3,5,2,1,4]
print(cycle_sort(arr))
