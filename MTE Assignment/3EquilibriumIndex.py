def equlibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
arr = [1,2,3,4,5]
print(equlibrium_index(arr))
arr = [-7, 1, 5, 2, -4, 3, 0]
print(equlibrium_index(arr))