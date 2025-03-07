def searchMatrix(matrix,target):

    
    s,e = 0 ,len(matrix)-1
    columns_len = len(matrix[0])
    
    c = 0
    mid = (s+e)//2

    if target > matrix[e][columns_len-1] or target < matrix[0][0]:
        return False 
    while c < columns_len :

        if target >= matrix[mid][c] and target <= matrix[mid][columns_len-1]:
            l,r = 0,columns_len-1
            while l <= r :
                m = (l+r)//2
                if matrix[mid][m] == target:
                    return True
                elif matrix[mid][m] >target :
                    r= m-1

                else : l= mid+1
            return False

        elif  target >= matrix[mid][columns_len-1]:
            mid = mid +1
        else : mid = mid-1


   

target = 15
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
ans = searchMatrix(matrix,target)
print(ans)