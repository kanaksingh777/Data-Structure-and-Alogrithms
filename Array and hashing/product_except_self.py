def prodexceptself(nums):

    prefix_array = []

    suffix_array = []
    
    res = []
    for i in range(len(nums)) :
        if i == 0 :
            prefix_array.append(1)
            continue
        prod =1
        for j in range(i,0,-1):

            prod = prod * nums[j-1]

        prefix_array.append(prod)
    
    for i in range(len(nums)):
        prod_2 = 1
        for j in range(i,len(nums)):
            if j == len(nums)-1:
                suffix_array.append(prod_2)
                continue
            prod_2 = prod_2 * nums[j+1]

    for i in range(len(prefix_array)):

        res.append(prefix_array[i] * suffix_array[i])

    return res


nums = [-1,0,1,2,3]
ans = prodexceptself(nums)
print(ans)