def l_s(nums):
    hashset = set(nums)
    longest = 0


    for n  in nums:
        if n-1 in hashset:
            continue
        length  = 1

        while (n+length in hashset):

            length +=1 

        longest = max(longest,length )

    return longest

        

nums = [0,3,2,5,4,6,1,1]

ans = l_s(nums)

print(ans)