

def skip_a(p,up):
    if not up:
        return p 

    
    ch = up[0]
    if ch == 'a':
        return  skip_a(p,up[1:])
    
    else: return skip_a(p+ch,up[1:])
    

s = "baccad"
print(skip_a("",s))