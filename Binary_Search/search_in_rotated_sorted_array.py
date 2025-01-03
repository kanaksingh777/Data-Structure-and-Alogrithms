# def rotated_sorted_array(nums,target):
#     l, r = 0, len(nums)-1

#     while l <=r :
#         mid = (l +r)//2
#         if nums[mid] > nums[mid+1]:
#             #this is the pivot element
#             return mid 
#         elif nums[mid] > nums[r]:
#             l = mid+1
#         else: r = mid
#     print(mid)
#     print(nums[mid])



# nums = [7,0,1,2]

# target = 3

# ans =rotated_sorted_array(nums,target)
# print(ans)
def rotated_sorted_array(nums,target):

    l,r = 0,len(nums)-1

    while l <= r:

        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        elif  (target >= nums[l] and target < nums[mid]):
            r = mid
        else:
            l = mid+1
    return -1

nums = [5,1,3]
target = 5
ans = rotated_sorted_array(nums,target)
print(ans)
