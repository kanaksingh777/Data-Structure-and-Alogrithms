def max_sum_subarray(nums):

    sum_s = 0
    max_s = 0

    for i in range(len(nums)):
            if nums[i] >= 0 :
                sum_s  += nums[i]
                max_s = max(sum_s, max_s)
            
    return max_s


nums = [-2,1,-3,4,-1,2,1,-5,4]
#sorted_nums = [-3,-2,0,1,3,4]
ans = max_sum_subarray(nums)
print(ans)