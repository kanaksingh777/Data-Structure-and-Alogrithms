
from collections import defaultdict
def long_cons_sequence(nums):
    hashmap = defaultdict(list)
    for num in nums:
        if (num-1) not in nums and  num not in hashmap.keys() :
        

            for i in range(len(nums)):
                next_num =num+i
                if (next_num) in nums:
                    hashmap[num].append(next_num)
                else : break
        else : continue

    max_len = max(len(v) for v in hashmap.values())  

    return max_len


nums = [9,1,4,7,3,-1,0,5,8,-1,6]
ans = long_cons_sequence(nums)
print(ans)