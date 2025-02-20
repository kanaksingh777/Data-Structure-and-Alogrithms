def two_sum(nums,target):


    prev_nums = {}

    for i in range(len(nums)):

        diff = target - nums[i]

        if diff not in prev_nums:
            prev_nums[nums[i]] = i
        else: 
            return [prev_nums[diff],i]
        

nums = [3,3]
target = 6

ans = two_sum(nums,target)
print(ans)