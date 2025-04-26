def two_sum(nums,target):
    #T.C=S.C=O(n)
    num_map = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement] , i]
        num_map[num] = i
    return []
nums = [2,7,9,11]
target = 11
print(two_sum(nums,target))