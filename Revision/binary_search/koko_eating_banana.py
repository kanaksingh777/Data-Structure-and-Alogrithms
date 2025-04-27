import math
def koko(piles,h):

    max_k =  max(piles)

    s, e  =1,max_k
    res = max(piles)
    while s <= e :

        mid = (s + e) //2 
        hours = 0
        for i in piles:
            hours +=  math.ceil (i/mid)
        if hours <= h :
            res  = min(res,mid)

            e = mid -1
        else: s = mid+1

    return res        

piles =  [25,10,23,4]
h =4    
ans = koko(piles,h)
print(ans)