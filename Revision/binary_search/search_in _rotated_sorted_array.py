def search_rotated_array(nums):

    res = nums[0]

    l,r = 0,len(nums)-1

    while l <= r :

        if nums[l] < nums[r] :
            res = min(res,nums[l])
            break
        mid = (l+r)//2

        res  = min(res,nums[mid])
        if nums[mid] >= nums[l]:
            
            l = mid+1
            
        else:  
            
            r = mid-1

    return res




nums = [2,1]

print(search_rotated_array(nums))
