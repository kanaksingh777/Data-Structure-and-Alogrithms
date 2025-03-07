def check_permutation(s1,s2):

        if len(s1) > len(s2):
            return False

        char_s1 = {}
        char_s2 = {}


        window_size = len(s1)
        

        #putting char of s1 in char_s1

        for i in s1:
            char_s1[i] = char_s1.get(i,0) +1


        for i in range(len(s2)-window_size+1):

            for r in range(i,window_size+i):

                char_s2[s2[r]] = char_s2.get(s2[r],0) +1

            if char_s1 == char_s2:
                return True
            else: 
                char_s2 = {}
                continue

        return False

            
s1 = "abc"
s2 = "leccbca"
ans = check_permutation(s1,s2)

print(ans)


