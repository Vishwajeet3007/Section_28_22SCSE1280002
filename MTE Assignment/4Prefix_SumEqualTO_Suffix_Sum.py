def can_be_split(arr):
    total_sum = sum(arr)
    prefix_sum = 0
    for i in range(len(arr)-1): # (-1 because at least 1 element in suffix_sum)
        prefix_sum += arr[i]
        suffix_sum = total_sum - prefix_sum
        if prefix_sum == suffix_sum:
            return True
    return False
arr = [1, 2, 3, 4, 6]
print(can_be_split(arr))
arr = [1, 2, 3, 4, 5, 5]
print(can_be_split(arr))