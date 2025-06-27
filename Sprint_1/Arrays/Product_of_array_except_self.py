

def Prod_arr_except_self(nums):
    prefix = []
    suffix = []
    for i in range(len(nums)):
        ans = 1
        for j in range(i-1,-1,-1):
            ans = nums[j] * ans 

        prefix.append(ans)
    
    for idx in range(len(nums)):
        ans =1
        for z in range(idx+1,len(nums)):
            ans = nums[z] *ans

        suffix.append(ans)

    
    ans_list = []
    for i in range(len(prefix)):
        ans_list.append(prefix[i]*suffix[i])

    return ans_list


nums = [1,2,4,6]

#prefix = [1,1,2,8]
# suffix =  
print(Prod_arr_except_self(nums))

# output - [i,- product of all the elem's except the number at this position]

#at each position , calculate the prefix , and the suffix