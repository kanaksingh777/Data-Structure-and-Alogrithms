def sequence(nums):
      
    num_set = set(nums)

    longest  = 0
    for  i in range(len(nums)):

        left_neighbor = nums[i] -1 
        if left_neighbor in num_set:
            continue

        sequence_length =1

        curr_num = nums[i]
        while True:

            if curr_num+1  in num_set:

                sequence_length +=1
                curr_num+=1
            
            else: break
        longest = max(sequence_length,longest)

    return longest



nums = [0,0]
ans = sequence(nums)
print(ans)