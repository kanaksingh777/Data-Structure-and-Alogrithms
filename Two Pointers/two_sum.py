def two_sum(nums,target):

    l,r = 0,1
    while l<r:

        while nums[l] == nums[r]:

            l= l+1
            r= r+1 

        while r <= len(nums)-1:

            if nums[l] + nums[r] == target:
                return nums[l] + nums[r]
            else : r =r+1
        l,r = l+1 ,l+2

        


target = 6

ans = two_sum(nums,target)