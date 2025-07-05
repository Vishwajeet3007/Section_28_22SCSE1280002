def rob(nums) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n  # We only need n slots
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        steal = nums[i] + dp[i - 2]
        skip = dp[i - 1]
        dp[i] = max(steal, skip)
        
    return dp[n - 1]
nums = [1,2,3,1]
print(rob(nums))