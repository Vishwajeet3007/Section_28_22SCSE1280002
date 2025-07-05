def subsets(nums):

    #T.C=S.C = O(n*2^n)
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result
nums = [1,2,3]
print(subsets(nums))
nums = [0]
print(subsets(nums))

# Using Bit Manipulation
def subsets(nums):
    n = len(nums)
    result = []
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])
        result.append(subset)
    return result
