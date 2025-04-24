from collections import deque
def maxSlidingWindow(nums,k):
    n = len(nums)
    result = []
    dq = deque()
    for i in range(n):
        if dq and dq[0] <= i-k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k-1:
            result.append(nums[dq[0]])
    return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))
nums = [1]
k = 1
print(maxSlidingWindow(nums,k))
