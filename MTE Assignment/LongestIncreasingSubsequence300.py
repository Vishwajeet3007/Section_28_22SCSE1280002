class Solution:
    def lengthOfLIS1(self, nums) -> int:
        n = len(nums)
        dp = [1] * n  # Every element is an LIS of at least 1
# T.C = O(n2) S.C=O(N) using Dp
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS1(nums))
# USing Dp NAd BinarySearch T.C=0(nlog(n)) S.C =O(n)

# from bisect import bisect_left

# class Solution:
#     def lengthOfLIS(self, nums) -> int:
#         sub = []
#         for num in nums:
#             i = bisect_left(sub, num)
#             if i == len(sub):
#                 sub.append(num)
#             else:
#                 sub[i] = num
#         return len(sub)

# print(Solution().lengthOfLIS(nums))