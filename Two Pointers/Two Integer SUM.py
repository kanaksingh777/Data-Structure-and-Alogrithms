def two_integers(nums,target):


    # a sorted array , two integers will sum for the target 

    # two pointer approach 

    s, e = 0, len(nums)-1

    while s < e : 
        sum = nums[s] + nums[e]
        if sum == target:
            return [s,e]
        
        elif sum > target : 
            e =e-1 

        else: s = s+1
    




nums = [1,3,4,5,7,11]

target = 9


ans = two_integers(nums,target)
print(ans )