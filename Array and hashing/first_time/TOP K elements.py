
# will comeback will do key as the number of times it occurs and the value as the numbers 

def topkelement(arr,k):

    hashmap = {}
    
    ans = []

    for i in arr: 
        if i in hashmap:
            hashmap[i]+=1 
        else : 
            hashmap[i] +=1

    
    for key,value in hashmap.items():
        if value >= k:
            ans.append(key)

    return ans  



nums = [1,22,2,2,2,10000000]

an = topkelement(nums,1)
print(an)