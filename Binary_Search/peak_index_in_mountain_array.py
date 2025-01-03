# def peak_index_in_mountain_arr(nums):

#     s,e = 0,len(nums)-1

#     while s < e :

#         mid = (s+e)//2

#         if (nums[mid] > nums[mid+1]):
#             e = mid

#         else: s= mid+1 # which means that this can be a potential peak element

#     return nums[e]




# nums = [6,3,2,1]

# ans = peak_index_in_mountain_arr(nums)
# # print(ans)


# def mountain_array(nums):

#     l,r = 0, len(nums)-1

#     while l < r :

#         mid = (l+r)//2
        

#         if nums[mid] > nums[mid+1]:
#             r = mid

#         else:  l = mid+1
#     return nums[r]
    
# arr = [7,9,4,2,1,0]
# #arr = [0,1,2,3,9,12,18,17,2,1]
# ans =  mountain_array(arr)
# print(ans)
def  mountain_array(nums):
    l,r = 0,len(nums)-1

    while l <=r:
        mid = (l+r)//2

        if nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] > nums[l]:
            l= mid+1
        else: r = mid 

arr = [9]
#arr = [0,1,2,3,9,12,18,17,2,1]
ans =  mountain_array(arr)
print(ans)
