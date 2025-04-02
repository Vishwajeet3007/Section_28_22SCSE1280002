def pivotElement(arr):
    left = 0
    right = len(arr) - 1
    while left < right :
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid+1
        else:
            right = mid
    return left
arr = [9,10,11,2,4,6,8]
print(pivotElement(arr))
arr = [3,4,0,1,2]
print(pivotElement(arr))