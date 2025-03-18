def twoSum(arr,target):
    
    # Using  Two pointer
    arr.sort()
    left  = 0
    right = len(arr)-1
    
    while  left < right:
        result = arr[left] + arr[right]
        if result == target:
            return "YES"
        if result < target:
            left += 1
        elif result > target :
            right -= 1
    return "NO"
arr = [4,6,8,4,2]
target = 14
print(twoSum(arr,target))
