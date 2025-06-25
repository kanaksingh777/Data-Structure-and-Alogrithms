from collections import defaultdict
def group_anagrams(strs):

    
    hashmap = defaultdict(list)
    for str in strs:
        n = [0]* 26
        for char in str:
            n[ord(char)-ord('a')] += 1
        hashmap[tuple(n)].append(str)


    return list(hashmap.values())


strs = ["act","pots","tops","cat","stop","hat"]

group_anagrams(strs)