# # fav_book = {'title':'xyz',
# #           'author':'author_name',
# #           'year':1991}
# # print(fav_book['title'])

# # fav_book['year']=2023
# # print(fav_book.items())

# # fav_book['genre'] = 'fiction'

# # fav_book.pop('author')
# # print(fav_book.items())

# # if 'publisher' not in fav_book.keys():
# #     fav_book['publisher'] ='unknown'

# # fav_book.update({'rating': 4.5, 'language': 'English'})

# # fav_book.clear()
# # library = {
# #     'Book1': {'title': 'xyz', 'author': 'author_name', 'year': 1991},
# #     'Book2': {'title': 'abc', 'author': 'another_author', 'year': 2000}
# # }

# # for key,val in library.items():
# #     if key == 'Book2':
# #         print(key['title'])
# #     else:
# #         continue


# # hashmap = {}

# # for i in range(1,6):
# #     hashmap[i] = i*i

# # print(hashmap)
# add_ten = lambda x: x + 10
# print(add_ten(5))  # Output: 15
hashmap = {}
for i in range(1,6):
    hashmap[i] = i*i
print(hashmap)
s = 0
for k,v in hashmap.items():
    s+=v

print(s)
