import collections
# do the question of returning the sequence rather than return the length only 


def longest_seq(nums):
    #creating a set for the arr
    numSet = set(nums)
    longest = 0 

    for n in nums:
        # check if n has a left neighbour in numSet
        if (n-1) not in numSet:
            length = 0 
            while (n + length) in numSet:
                length  += 1 

            longest =max(length,longest)

    return longest 


            











arr = [100,4,200,1,3,2]
longest_seq(arr)