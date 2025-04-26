def max_subarray_sum(arr):
    max_curr = max_global = arr[0]
    for i in range(1,len(arr)):
        max_curr = max(arr[i],max_curr + arr[i])
        if max_curr > max_global:
            max_global = max_curr
    return max_global
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))