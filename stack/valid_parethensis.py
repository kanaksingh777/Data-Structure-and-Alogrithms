def validPara(s):


    stack = []
    hashmap = { '}' : '{', ')':'(' , ']':'['}


    for c in s :
        if c in hashmap:
            if stack and stack[-1] != hashmap[c] :
                return False
            else : stack.pop()
        else :stack.append(c)

    return True if not stack else False


s ="]"
print(validPara(s))



