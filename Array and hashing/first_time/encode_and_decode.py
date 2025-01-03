def encode(s1):

    res = []
    string = ""
    for s in s1:
        string += s + str(len(s)) + '#'

    temp = ""
    
    for i,char in enumerate(string):
        if (char.isdigit()) and string[i+1] =='#':

            res.append(temp)
            temp=""

        else : temp += char

            









s1 = ["neet","code","love","you"]


encode(s1)

