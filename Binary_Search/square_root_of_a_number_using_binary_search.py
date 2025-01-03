def precise_sq_root(num,precision,integer):

    precise_ans = integer
    fraction = 1
    for i in range(precision):
        fraction = fraction /10
        #0.1

        #now i need to keep on adding this fraction to the the integer number to check if a new decimal number equals to the square root

        while (precise_ans + fraction) * (precise_ans + fraction) <= num:
            precise_ans += fraction
    return round(precise_ans,precision)





def square_root(num,precision):  
    # only valid if a number is a integer not a decimal number

    l ,r =1,num//2
    sqr_root = 0

    while l<=r : 
        mid = (l+r)//2

        if  mid * mid  < num :
            sqr_root = mid
            l = mid +1
        elif mid *mid > num:
             r  = mid-1
            
        else:
            sqr_root = mid
            break
    ans = precise_sq_root(num,3,sqr_root)

    return ans 
    


    
num = 22
sq= square_root(num,3)
print(sq)
