# given a string check if it is a valid pallindrome 
def valid_pallidrome(s):
    l,r = 0, len(s)-1

    while l < r : 
        while l < r and not isalphanumeric(s[l]):
            l +=1
        while l < r and not isalphanumeric(s[r]):
            r -= 1

        
        

        if s[l].lower() == s[r].lower():
            l +=1 
            r -=1

        else: return False
    return True





def isalphanumeric(c):

    if( ord('A') <= ord(c) <= ord('Z') or 
                    ord('a')<=ord(c)<= ord('z') or 
                    ord('0')<= ord(c)<= ord('9'))== True:
        
        return True
        

s = "Was it a car or a cat I saw?"


ans = valid_pallidrome(s)
print(ans)