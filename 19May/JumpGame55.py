def canJump(nums):
    max_jump = 0
    for i in range(len(nums)):
        if i > max_jump:
            return False
        max_jump = max(max_jump,i+nums[i])
    return True
nums = [2,3,1,0,4]
print(canJump(nums))
nums = [3,2,1,0,4]
print(canJump(nums))