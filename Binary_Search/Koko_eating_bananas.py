import math
def koko_eating_banana(piles,h):

    max_k = max(piles)


    s,e = 1,max_k
    res =   e
    while s < e :

        k = (s+e)//2

        max_hours = 0
        for i in piles :
            
            max_hours += math.ceil(i/k)

        if max_hours < h:
            res = min(res,max_hours)
            e  = k-1
        else:
            s= k+1
    return res 

piles = [3,6,7,11] 
h =8

returns_k = koko_eating_banana(piles,h)

print(returns_k)
