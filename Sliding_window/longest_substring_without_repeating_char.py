def l_s(s):
    charSet =  set()

    l = 0
    res = 0 
    for r in range(len(s)):
      
        while s[r] in charSet:
         
            charSet.remove(s[l])

            l += 1
        charSet.add(s[r])
        res = max(res,r-l+1)
    
    return res



s = "pwwkew"
ans = l_s(s)
print(ans)