
s = [[1,2,3],
     [4,5,6]]

rows = {}

for i in range(len(s)+1):
    for j in range(i):
        if s[i] not in rows.keys():
            rows[i] = rows.get(i,0) +s[i]