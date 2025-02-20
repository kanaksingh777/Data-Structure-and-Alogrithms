from collections import defaultdict
def groupAnagram(str):

    hashmap  = defaultdict(list)
  

    for str in strs:
        count = [0]*26
        for c in str:
            count[ord(c) - ord("a")] += 1

        hashmap[tuple(count)].append(str)
    
    return hashmap.values()



strs = ["act","pots","tops","cat","stop","hat"]

ans = groupAnagram(strs)
print(ans)