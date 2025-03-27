def pivotElement(arr):
    left = 0
    right = len(arr) - 1
    while left < right :
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid+1
        else:
            right = mid
    return arr[left-1]
arr = [9,10,11,2,4,6,8]
    
print(pivotElement(arr))

