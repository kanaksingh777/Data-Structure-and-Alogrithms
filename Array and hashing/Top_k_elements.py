


def top_k_elems(nums,k):
    hashmap ={}

    freq_elements = [[] for i in range(len(nums)+1)]
    
    for  i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i],0) +1 

    for k,v in hashmap.items():
        freq_elements[v].append(k)

    res = []

    for  i in range(len(freq_elements)-1,0,-1):
        for n in freq_elements[i]:
            res.append(n)
            if len(res) == k:
                return res
            



nums = [1,1,1,2,2,3]
k = 2
top_k_elems(nums,k)