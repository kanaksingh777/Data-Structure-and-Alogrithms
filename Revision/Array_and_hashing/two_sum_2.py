def two_sum(nums,target):

    l=0

    while l < len(nums)-1:
        r= l+1
        while r < len(nums):

            if nums[l] + nums[r] == target :
                return [l,r]
            else:
            
                r = r+1
        l +=1
    return -1            


nums = [1,2,3,4]

target  =4
print(two_sum(nums,target))
