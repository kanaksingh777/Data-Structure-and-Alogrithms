
def prod_except_self(nums):

    pref_array = []  #calculating prefix and suffix at each position
    suffix_array = []
    

    for i in range(len(nums)):
        if i == 0 :
            pref_array.append(1)
            continue
        prod = 1
        for j in range(i,0,-1):
            prod = prod * nums[j-1]

        pref_array.append(prod)

    for i in range(len(nums)):
        if i == len(nums):
            suffix_array.append(1)
            break
        prod = 1
        for j  in range(i+1,len(nums)):

            prod = prod * nums[j]

        suffix_array.append(prod)

    res = []

    for i in range(len(pref_array)):
        res.append(pref_array[i] * suffix_array[i])

    return res


nums = [1,2,4,6]


print(prod_except_self(nums))