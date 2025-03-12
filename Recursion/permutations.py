# permutation of string 'abc'
def permutation(p,up):
    if not up:
        print(p)
        return 
    
    ch = up[0]

    for  i in range(len(p)+1):

        new_p = p[:i] +[ch] + p[i:]

        permutation(new_p,up[1:])





s =  [1,2,3]

permutation([],s)