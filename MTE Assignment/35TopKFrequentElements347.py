from collections import Counter
def topKfrequent(nums,k):
    #T.C=O(nlogk)
    freq = Counter(nums)
    sorted_items = sorted(freq.items() ,key = lambda x:x[1],reverse=True)
    result = [item[0] for item in sorted_items[:k]]
    return result
nums = [1,1,1,2,2,3]
k = 2
print(topKfrequent(nums,k))
nums = [1]
k = 1
print(topKfrequent(nums,k))
