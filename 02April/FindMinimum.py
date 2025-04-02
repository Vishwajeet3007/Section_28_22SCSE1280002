def minelement(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right -left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

arr = [8,9,0,1,2,3,4,5,6,7] 
print(minelement(arr))