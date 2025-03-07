def valid_pallindrome(s):



        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


s = "Was it a car or a cat I saw?"

ans = valid_pallindrome(s)