def three_sum(nums):

    nums.sort()
    res = [[]]
    for i in range(len(nums)-1):

        l,r = i+1,len(nums)-1

        while l < r:
            if nums[l] + nums[r] > nums[i]:

                r -= 1

            elif nums[l] + nums[r] < nums[i]:
                l = l+1

            else :
                res.append([nums[i],nums[l],nums[r]])
                l=l+1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
                    
    return res

nums = nums=[-1,0,1,2,-1,-4]

ans = three_sum(nums)
print(ans)