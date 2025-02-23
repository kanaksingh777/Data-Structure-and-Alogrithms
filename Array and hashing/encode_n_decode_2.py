def encode(l):
    res = ""

    for s in l:
        res += str(len(s)) +'#' + s
    decode(res)

# def decode(str):
#     res , i  = [],0
#     while i < len(str):
#         j=i 
#         while str[j] != '#':
#             j +=1 
#             length = int(str[i:j])
#             res.append(str[j+1 : j+1+length])

#             i= j+1+length

def decode(str):
    



   
ia =  ["neet","code","love","you"]

encode(ia)