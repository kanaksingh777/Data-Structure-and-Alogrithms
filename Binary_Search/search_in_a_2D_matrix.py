def search_2d_matrix(matrix,target):
    s,e = 0, len(matrix)-1
    while s<=e :
    
        r_mid = (s+e)//2
          # this mid is the row
        print(matrix[r_mid][0])
        print(matrix[r_mid][-1])

        if target >= matrix[r_mid][0] and target <= matrix[r_mid][-1]:


            l,r = 0, len(matrix[r_mid])

            while l<=r :
                m = (l+r)//2
                print(matrix[r_mid][m])
                if matrix[r_mid][m] > target :
                    r = m-1

                elif  matrix[r_mid][m] < target:
                    l=  m +1
                else : return True
            return False

        elif target > matrix[r_mid][-1]:
            s = r_mid +1

        else : e = r_mid-1

    return False
#matrix= [[1,2,3,4],[5,6,7,12],[22,24,29,30]]
matrix =[[1]]
target = 0
ans = search_2d_matrix(matrix,target)
print(ans)