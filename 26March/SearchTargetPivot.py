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
def Bs(arr,left,right,target):
    while left <= right:
        mid = left + (right - left )//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 
    return -1
def search_element(arr,target):
    if not arr:
        return -1
    pivot = pivotElement(arr)
    if arr[pivot] == target:
        return pivot
    if target >= arr[pivot] and target <= arr[-1]: 
        return Bs(arr,pivot,len(arr)-1,target)
    else:
        return Bs(arr,0,pivot-1,target)
arr = [7,9,1,2,3]
target = 3
print(search_element(arr,target))
    
