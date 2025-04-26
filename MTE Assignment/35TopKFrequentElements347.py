from collections import Counter
import heapq
def topKfrequent(nums,k):
    freq_map = Counter(nums)
    heap = [(-freq,num) for num , freq in freq_map.items()]
    result = []
    for _ in range(k):
        freq,num = heapq.heappop(heap)
        result.append(num)
    return result
    
nums = [1,1,1,2,2,3]
k = 2
print(topKfrequent(nums,k))
nums = [1]
k = 1
print(topKfrequent(nums,k))
