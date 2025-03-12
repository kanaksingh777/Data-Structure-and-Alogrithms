def subsets(up):
    
    
    ans = []

    def helper(p,up):
        if not up :
            
            return ans.append(p)
        
        ch = up[0]

        helper(p+ch,up[1:])

        helper(p,up[1:])
        
        return ans[:-1]

    return helper("",up)
        

s = "abc"
print(subsets(s))





    

