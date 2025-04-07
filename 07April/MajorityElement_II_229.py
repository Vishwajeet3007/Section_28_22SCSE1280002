from collections import Counter
def MajorityElement2(nums):
    #Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

    # Time and Space Complexity  = O(n)

    # freq = Counter(nums)
    # return [num  for num , count in freq.items() if count > len(nums) // 3]

    count1 =0
    count2 = 0
    cand1 ,cand2 = None,None
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1 ,count1 = num , 1
        elif count2 == 0:
            cand2 , count2 = num,1
        else:
            count1 -= 1
            count2 -= 1
    result = []
    for candidates in [cand1,cand2]:
        if nums.count(candidates) > len(nums) // 3:
            result.append(candidates)
    return result


nums = [3,2,3]
print(MajorityElement2(nums))
nums = [1,2]
print(MajorityElement2(nums))
nums = [1]
print(MajorityElement2(nums))

