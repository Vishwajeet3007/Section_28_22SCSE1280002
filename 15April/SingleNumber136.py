def SingleNumber(nums):
    unique = 0
    for num in nums:
        unique ^= num
    return unique
nums = [2,2,1]
print(SingleNumber(nums))
nums = [4,1,2,1,2]
print(SingleNumber(nums))
nums = [1]
print(SingleNumber(nums))