def SubarraySumEqualK(nums,k):
# Brute Force T.C=O(N*N) S.C = O(1)

    # n = len(nums)
    # count = 0
    # for start in range(n):
    #     total = 0
    #     for end in range(start,n):
    #         total += nums[end]
    #         if total == k:
    #             count += 1
    # return count

    # Using Hashing T.C=S.C=O(n)
    count = 0
    curr_sum = 0
    prefix_sum = {0:1}
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sum:
            count += prefix_sum[curr_sum - k]
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0) + 1
    return count

nums = [1,1,1]
k = 2
print(SubarraySumEqualK(nums,k))
nums = [1,-1,0]
k = 0
print(SubarraySumEqualK(nums,k))