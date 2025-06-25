def longest_repeating_charac(s,k):

    hashmap = {}

    l = 0 
    res = 0 
    for r in range(len(s)):

        hashmap[s[r]] = hashmap.get(s[r],0)+1

        if (r-l+1) - max(hashmap.values()) > k:

            hashmap[s[l]] -=1 

            l = l+1

        res = max(res,r-l+1)

    return res

s = "AAABABB"
k =2

print(longest_repeating_charac(s,k))