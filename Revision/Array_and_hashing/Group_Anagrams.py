from collections import defaultdict
def group_anagrams(strs):

    hashmap = defaultdict(list)


    for str in strs :
        count = [0] * 26 

        for char in str:
            count[ord(char)- ord('a')] +=1

        hashmap[tuple(count)].append(str)

    return hashmap.values()




strs = ["act","pots","tops","cat","stop","hat"]

ans = group_anagrams(strs)

print(ans)