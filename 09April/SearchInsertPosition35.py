def searchPosition(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
    # return arr.index(target)
nums = [1,3,5,6]
target = 5
print(searchPosition(nums,target))
nums = [1,3,5,6]
target = 2
print(searchPosition(nums,target))
nums = [1,3,5,6]
target = 7
print(searchPosition(nums,target))