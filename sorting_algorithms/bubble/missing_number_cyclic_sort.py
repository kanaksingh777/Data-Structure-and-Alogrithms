def missing_num(nums, n):
    i = 0
    while i < len(nums) :

        if nums[i] != i and nums[i] < len(nums):
            
            temp = nums[i]

            nums[i] = nums[nums[i]]

            nums[temp] = temp 

        else : i = i+1

    for miss in range(len(nums)):
        if  nums[miss] != miss:
            return miss
    return len(nums)

arr = [0,1]
n =5
print(missing_num(arr,n))