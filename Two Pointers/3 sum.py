def three_sum(nums):
    nums.sort()
    res = []
    l,r =1,len(nums)-1
    for i in range(len(nums)-1):
            l,r =i+1,len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue 
                
            while l < r :


                    if nums[i] + nums[l] + nums[r] == 0 :
                        res.append([nums[i],nums[l],nums[r]])

                        while nums[l] ==nums [l+1] and l < r-1 :
                            l = l+1
                        l=l+1

                    elif nums[i] + nums[l] + nums[r] > 0 :
                        r = r-1

                    else : l +=1
            
    return res
nums = [0,0,0]
ans = three_sum(nums)
print(ans)


