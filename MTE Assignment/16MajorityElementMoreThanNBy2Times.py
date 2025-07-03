from collections import Counter
def majorityElement(nums):
    # Using HashMap  T.C = S.C =O(n)
    # freq = Counter(nums)
    # for num in freq:
    #     if freq[num] > len(nums) // 2:
    #         return num

    # Using Boyer-Moore Voting Algorithm
    count = 0
    candidate = None
    for i, num in enumerate(nums):
        if count == 0:
            candidate = num
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return candidate


        
    # USing 
nums = [1,2,2,4,5,2,2,1,2]
print(majorityElement(nums))

    # Using Boyer-Moore Voting Algorithm
    
