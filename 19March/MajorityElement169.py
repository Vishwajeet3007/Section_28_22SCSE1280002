from collections import Counter
def majorityElements(nums):
    freq =  Counter(nums)
    for ch in freq:
        if freq[ch] > len(nums) // 2:
            return ch
nums = [3,2,3]
print(majorityElements(nums))
