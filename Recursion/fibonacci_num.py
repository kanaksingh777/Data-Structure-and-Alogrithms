#fibo and #binary search def fibo(n):
def fibo(n):
    if n == 0:
        return 0
    
    if n == 1 :
        return 1 
    
    ans = fibo(n-1) + fibo(n-2)
    return ans


n = 6
print(fibo(n))