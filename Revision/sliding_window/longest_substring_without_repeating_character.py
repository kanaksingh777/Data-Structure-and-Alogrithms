def longest_sub_without_duplicate(s):
    res = 0
    charset = set()
    l = 0 
    for r in range(len(s)):

        if s[r] not in charset:
            charset.add(s[r])
            res = max(res,r-l+1)

        else:
            while s[r] in charset:
                charset.remove(s[l])
                l = l+1
    return res

s = "xxxx"

print(longest_sub_without_duplicate(s))
