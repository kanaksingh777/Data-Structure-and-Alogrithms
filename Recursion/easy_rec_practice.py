# # n to 1 
# def printnum(n):

#     if n == 0 :
#         return 
    
#     print(n)
#     printnum(n-1)



# n=5
# printnum(n)

# 1 to n 

# def print1ton(n):
#     if n == 0 :
#         return 
    
#     print1ton(n-1)
#     print(n)
    

# n=5
# print1ton(n)

# def fact(n):

#     if n == 1 :
#         return 1
    
#     return n * fact(n-1)

# ans = fact(5)
# print(ans)


#sumofdigits -- n =1342

# def sum_of_digits(n):
#     if n//10 == 0:
#         return n
    

#     num = n % 10

#     rem_num = n //10

#     return num + sum_of_digits(rem_num)

# n = 55865
# ans = sum_of_digits(n)

# print(ans)

#sorted or not 

# def sorted(arr,l,r):

#     if r == len(arr):
#         return True

#     if arr[l] < arr[r]:
#        return sorted(arr,l+1,r+1)
#     else : return False




# arr = [3,41,222,5555,66666]
# ans = sorted(arr,0,1)
# print(ans)

#   

#returning it in the function argument 
# def srch(arr,t,i,ans):
#     if i == len(arr):
#        return ans 
    
#     if t == arr[i]:
       
#        ans.append(i)
    
#     return srch(arr,t,i+1,ans)




arr = [3,41,222,5555,66666,5555]

# print(srch(arr,5555,0,[]))

#returning it in the body 
z = []
def srch_2(arr,target,i):
   
    if i == len(arr):
        return z
    
    if arr[i] == target:
        z.append(i)


    return srch_2(arr,target,i+1)

print(srch_2(arr,5555,0))
