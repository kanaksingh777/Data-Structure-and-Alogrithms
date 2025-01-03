def three_sum(nums):
    nums.sort()

    for i,value in enumerate(nums): 
        l, r = 0 , len(nums)-1


        while l < r :

            sum = value + nums[l+1] + nums[r]

            if sum > 0 :
                r = r-1

            elif sum <0 :
                l = l+1
            else : 
                return[i,nums[l],nums[r]]

            


nums = [-1,0,1,2,-4]
ans = three_sum(nums)
print(ans)


