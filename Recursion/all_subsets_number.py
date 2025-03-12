def subsets(p,up):
    if not up:
        
        return a.append(p)
    first_num = up[0]
    
    subsets(p + [first_num],up[1:])

    subsets(p,up[1:])

    return a





nums = [1,2,3]
ans = []
a = []
print(subsets(ans,[1,2,3]))