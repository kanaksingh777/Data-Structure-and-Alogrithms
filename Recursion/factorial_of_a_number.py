#5! =5 X 4 X 3 X 2 X 1 

def factorial(n):
    if n==1:return 1 #defined the base condition


    fact = n  * factorial(n-1)
    # sum = n + sum(n-1) similarly we can calculate the sum as well .
    

    return fact


ans = factorial(5)

print(ans)