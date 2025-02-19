# print all the numbers from n till 1

# def pn(n):
#     if n <1:return 
#     print(n)

#     pn(n-1)
# pn(5)

#print all the number from 1 till n 
#print when we are emptying the stack 
 
def pn(n):
    if n==0:
        return 
    #print(n) --- going into each call 
    pn(n-1)
    print(n)

pn(5)
    