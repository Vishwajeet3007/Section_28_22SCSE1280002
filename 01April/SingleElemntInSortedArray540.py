def singleElement(nums):
    unique = 0
    for num in nums:
        unique ^= num
    return unique
nums = [1,1,2,3,3,4,4,8,8]
print(singleElement(nums))
nums = [3,3,7,7,10,11,11]
print(singleElement(nums))