
def isAnagram(s: str, t: str) -> bool:
        hashmap_s = dict()
        hashmap_r = dict()

        for char_s in s : 
            hashmap_s[char_s] = hashmap_s.get(char_s,0) + 1

        for char_r in t:
            hashmap_r[char_r] = hashmap_r.get(char_r,0)+1

        if hashmap_s == hashmap_r:
            return True
        else : 
            return False
        
s  = "carrace"
t  = "racecar"

ans =isAnagram(s,t)
print(ans)