def trapping_rain_water(heights):

    
    n = len(heights)
    
    if n==0 :
        return 0
    
    left_max = [0] * n
    right_max = [0] * n 
    left_max[0] = heights[0]
    right_max[n-1] = heights[n-1]
    
    #created a left max and a right max 
    
    for i in range(1,n):

        left_max[i]= max(left_max[i-1],heights[i])
         
    for i in range(n-2,-1,-1):
        
        right_max[i] = max(heights[i],right_max[i+1])
    res = 0
    for i in range(n):
        res += min(left_max[i],right_max[i]) - heights[i]
    return res 

        

heights = [0,2,0,3,1,0,1,3,2,1]
ans = trapping_rain_water(heights)

print(ans )
    
