def longest_substring(s):

    s_set = set()
    l,r = 0,0
    longest = 0
    


    for i,value in s: 
        if value in s_set:
            l = l+1
            r = r+1

            








s = 'abcabcbb'

ans = longest_substring(s)
print(ans)