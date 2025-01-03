


def maxArea(nums):

    max_area = 0

    
    l,r = 0,len(nums)-1
    while l < r:

        area = min(nums[l],nums[r]) * (r-l)
        max_area = max(max_area,area)
        if nums[r] > nums[l]:
            l=l+1
        else: r = r-1


    return max_area



nums =[1,8,2,3,4,6,7]

ans = maxArea(nums)

print(ans)