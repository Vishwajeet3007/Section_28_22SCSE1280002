def nearlysorted(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if mid > left and arr[ mid - 1] == target:
            return mid - 1
        if mid < right and arr[mid + 1] ==  target:
            return mid + 1
        if target < arr[mid]:
            right = mid - 2
        else:
            left = mid + 2
    return -1
arr = [2,6,4,10,8]
target = 8
print(nearlysorted(arr,target)) 