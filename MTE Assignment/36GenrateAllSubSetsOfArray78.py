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