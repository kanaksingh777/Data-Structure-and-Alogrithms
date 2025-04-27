def three_sum(nums):
    nums.sort()
    res =  []

    for i in range(len(nums)):
        if i >=1 and nums[i] == nums[i-1]:
            continue
        l,r = i+1 , len(nums) -1

        while l < r :
            


            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum < 0:
                l = l+1
            elif curr_sum > 0 :
                r =r -1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l = l +1
                r = r-1

                while nums[l] == nums[l-1] and l <r :
                    l = l+1

    return res
nums=[0,0,0,0]

print(three_sum(nums))

