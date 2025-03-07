def findMin(nums):
        s,e = 0 ,len(nums)-1



        while s <= e :
            
            mid = (s+e)//2

            if nums[mid] > nums[mid+1]: 
                return mid ,mid+1
            
            elif nums[mid] > nums[e]:
                 s = mid+1
            else : e = mid
                    

                

nums = [4,5,0,1,2,3]
pivot,min_num = findMin(nums)
print(pivot,min_num)


