def jump(nums):
    jumps = 0
    curr_jump = 0
    max_jump = 0
    for i in range(len(nums)-1):
        max_jump = max(max_jump , i + nums[i])
        if i == curr_jump:
            jumps += 1
            curr_jump = max_jump
    return jumps
nums = [2,3,1,4,1,1,1,2]
print(jump(nums))