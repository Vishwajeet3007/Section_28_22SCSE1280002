def twoSum(arr,target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False
arr = [3,6,8,4,2]
target = 7
print(twoSum(arr,target))
