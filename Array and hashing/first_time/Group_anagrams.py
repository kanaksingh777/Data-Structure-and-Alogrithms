from collections import defaultdict
def group_anagrams(strs):

    res = defaultdict(list)

    for s in strs:

        count = [0] * 26
        for c in s : 
            count[ ord(c) - ord('a')] += 1 

        res[tuple(count)].append(s)
        print(res)

    return res.values()
        


            
            
            

    


strs = ["act","pots","tops","cat","stop","hat"]

ans = group_anagrams(strs)

print(ans)