def JumpGame(nums):
    jump = 0
    curr_jump = 0
    max_jump = 0
    for i in range(len(nums)-1):
        max_jump = max(max_jump,i+nums[i])
        if i == curr_jump:
            jump += 1
            curr_jump = max_jump
    return jump
nums = [2,3,1,1,4]
print(JumpGame(nums))