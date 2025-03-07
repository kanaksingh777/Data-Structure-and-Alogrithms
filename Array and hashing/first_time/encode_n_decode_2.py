

def encode(strs):
        new_str = ""
        for s in strs:
            str_len = len(s)
            new_str += str (str_len) +"#" +s

        return decode(new_str)



        

def decode(s):
        
        res = []

        char= 0

        while char < len(s):
            j = char
            while s[j] != "#":
                  j += 1
                
            
            num = int(s[char:j]) 
            res.append(s[j+1 :j+1+num])

            char = j + 1 + num
        return res


strs = ["we","say",":","yes","!@#$%^&*()"]
ans = encode(strs)
print(ans)
#Output:["neet","code","love","you"]
