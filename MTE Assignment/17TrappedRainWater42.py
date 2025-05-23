def trap_Rain_water(heights):
    n = len(heights)
    left_max = [0] * n
    left_max[0] = heights[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],heights[i])
    
    right_max = [0] * n
    right_max[n-1] = heights[n-1]
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],heights[i])
    
    ans = 0
    for i in range(n):
        ans += min(left_max[i],right_max[i]) - heights[i]
    return ans
height = [4,2,0,3,2,5]
print(trap_Rain_water(height))
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_Rain_water(height))