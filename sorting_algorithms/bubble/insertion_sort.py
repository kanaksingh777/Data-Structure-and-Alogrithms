def insertion_sort(arr):

    for i  in range(len(arr)-1):

        for j in range(i+1,0,-1) :

            if arr[j] < arr[j-1]:

                arr[j],arr[j-1] = arr[j-1],arr[j]

            #s = arr[j-2]
          
                    

            else :break 
    return arr


arr = [3,1,7,4,5]
print(insertion_sort([3, 1, 2, 1, 3]))  # ✅ [1, 1, 2, 3, 3]
    
