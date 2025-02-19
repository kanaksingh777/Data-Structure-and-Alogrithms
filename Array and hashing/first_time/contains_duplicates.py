def duplicates(nums):

    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        else: hashset.add(i) 
    return False


nums = [1,2,3,3]

duplicates(nums)