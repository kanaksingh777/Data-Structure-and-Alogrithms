a = []
def maze(p,r,c):

    if r == 1 and c==1 :
        a.append(p)

    
    
    if r > 1 :
        maze(p +'V',r-1,c)

    if r >1 and c>1 :
        maze(p +'D',r-1,c-1)

    if c > 1 :
        maze(p+ 'H',r,c-1)

    

    return a






ans = maze("",3,3)
print(ans)