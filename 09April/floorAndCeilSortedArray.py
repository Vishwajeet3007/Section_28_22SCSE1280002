def getFloorAndCeil(arr,target):
    n = len(arr)
    floor = -1
    ceil = -1

    # Binary search for floor
    left = 0 
    right = n - 1
    while left <=  right:
        mid = left + (right - left) // 2
        if arr[mid] ==  target:
            floor = arr[mid]
            break
        if arr[mid] < target:
            floor = arr[mid]
            left = mid + 1
        else:
            right = mid - 1

    # Binary Search for ceil
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            ceil = arr[mid]
            break
        if arr[mid] > target:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return floor , ceil
arr = [3, 4, 4, 7, 8, 10]
target = 8
print(getFloorAndCeil(arr,target))
    