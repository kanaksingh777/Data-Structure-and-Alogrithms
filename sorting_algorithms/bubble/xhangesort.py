def bubble_sort(arr):
    j = 0
    arr_len = len(arr)
    while j < arr_len:
        swapped = False

    
        for i  in range(arr_len-1):
        
            if arr[i] > arr[i+1]:

                arr[i],arr[i+1] = arr[i+1],arr[i]

                swapped = True
        if not swapped :
            break
        arr_len = arr_len-1
        j = j+1
    return arr




arr = [3,1,5,4,2]
ans = bubble_sort(arr)