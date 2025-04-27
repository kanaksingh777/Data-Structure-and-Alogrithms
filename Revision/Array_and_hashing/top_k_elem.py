def top_k_elements(nums,k):


    count= {}

    freq = [[] for i in range(len(nums)+1)]

    for num in nums:

        count[num] = count.get(num,0)+1

    for k,v in count.items():

        freq[v].append(k)

    res = []
    for i in range(len(freq)-1,0,-1):
        for num in freq:
            res.append(num)
            if len(res) == k:
                return res
            


nums = [1,1,2,2,3,3,3,3]
top_k_elements(nums,2)