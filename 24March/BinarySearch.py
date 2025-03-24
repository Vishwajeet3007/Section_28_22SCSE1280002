# def binarySearch(arr,target):
#     arr.sort()
#     start , end = 0 , len(arr) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1

def binarySearch(arr,start,end,target):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearch(arr,mid + 1 , end,target)
    else:
        return binarySearch(arr,start,mid - 1,target)

arr = [10,20,30,40,50,60]

print(binarySearch(arr,0,len(arr)-1,20))