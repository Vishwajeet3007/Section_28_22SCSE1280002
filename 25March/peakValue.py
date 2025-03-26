def peakValue(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = left +  (right - left) // 2
        if arr[mid] > arr[mid+1]:
            right = mid
        else:
            left = mid +  1
    return arr[left]
arr = [0,1,5,11,12,]
print(peakValue(arr)) 