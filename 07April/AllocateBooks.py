def findPages(arr,m):
    if m > len(arr):
        return -1
    def is_possible(arr,m,mid):
        students = 1
        curr_page = 0
        for pages in arr:
            if pages > mid:
                return False
            if curr_page + pages > mid:
                students += 1
                curr_page = pages
                if students > m:
                    return False
            else:
                curr_page += pages
        return True

    low = max(arr)
    high = sum(arr)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr,m,mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
arr = [12, 34, 67, 90]
m = 2
print(findPages(arr,m))
arr = [25, 46, 28, 49, 24]
m = 4
print(findPages(arr,m))
