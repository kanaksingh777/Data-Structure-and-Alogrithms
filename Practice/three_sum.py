def threeSum(nums):
    nums.sort()
    res = []

    for i,v in enumerate(nums):
        if i > 0 and v == nums[i-1]:
            continue

        l,r  = i+1, len(nums)-1

        while l < r :
            three_sum = nums[i] + nums[l] + nums[r]

            if(three_sum == 0):
                res.append([nums[i],nums[l],nums[r]])

                l+=1
                while nums[l] == nums[l-1] and l <r :
                    l+=1

                

            elif three_sum < 0: 
                l +=1

            else: r -=1

    return res
arr = [-1,0,1,2,-1,4]
ans = threeSum(arr)
print(ans)
