
#brute force 
# i need to return the k most frequent elements, 
# so i need to create a bucket or a array with the length of num list , and then add each num to its count
# count will be the index , like 2,3 will be siiting in index 4 , if they have occured 4 number of times in
#that array 

def top_k_elements(nums,k):

    count =  [[] for _ in range(len(nums))]
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num,0)+1

    for key, values in hashmap.items():
        count[values].append(key)
    res = []
    for i in range(len(count)-1,0,-1):
        if  count[i] :
            for z in count[i]:
                if k >= len(res):
                    res.append(z)
    return res 
nums = [1,2,2,2,3,3,3]
k=2
top_k_elements(nums,k)