s =  "was it a car or a cat i saw?"
n = len(s)

for i in range(n//2):
    if s[i]  != s[n-i-1]:
        #print("False")
        continue

print("True")