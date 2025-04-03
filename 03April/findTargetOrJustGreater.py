def findTargetOrJustGreater(arr,target):
    # Using Brute Force
    # for i in range(len(arr)):
    #     if arr[i] >= target:
    #         return arr[i]
    # return "Not found"

    left = 0
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            ans = arr[mid]
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return ans
arr = [1,2,8,9]
target = 7
print(findTargetOrJustGreater(arr,target))