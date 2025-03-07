def min_window_substring(s,t):
    if t == "":
        return ""
    
    countT,window = {} ,{}

    for c in t :
        countT[c] = countT.get(c,0) +1 

    have,need = 0,len(countT)
    res,resLen = [-1,-1] ,float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]

        window[c] = window.get(c,0) +1 

        if c in countT and window[c] == countT[c]:
            have +=1 
        
        while have == need :
            #update our result
            if (r-l+1) <resLen:

    


s = "OUZODYXAZV"
t = "XYZ"