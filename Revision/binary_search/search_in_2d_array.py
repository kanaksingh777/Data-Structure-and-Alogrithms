
def search_in_2d_matrix(matrix,target):


    row_s,row_e  = 0,len(matrix)-1
    
    while row_s <= row_e:
        mid_row = (row_s + row_e)//2 
        if target in matrix[mid_row]:
            s,e = 0,len(matrix[mid_row])-1
            
            while s <= e :
                mid = (s+e)//2

                
                elem = matrix[mid_row][mid]
                if target > elem :
                    s = mid +1 
                elif target < elem :
                    e = mid -1 

                else :return True
        elif target < matrix[mid_row][0]:
            row_e = mid_row -1

        else : row_s = mid_row +1

    return False


matrix =[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target =15
ans = search_in_2d_matrix(matrix,target)
print(ans)