def max_sum_subArray_k(nums,k):
    n = len(nums)
    if n < k:
        return -1
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k,n):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum,window_sum)
    return max_sum
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subArray_k(nums,k))
nums = [2, 1, 5, 1, 3, 2]
k = 2
print(max_sum_subArray_k(nums,k))