def prefix_sum(arr):
    # Using DP T.C = S.C = O(n)

    # prefix_sum = [0] * len(arr)
    # prefix_sum[0] = arr[0]
    # for i in range(1,len(arr)):
    #     prefix_sum[i] = prefix_sum[i-1] + arr[i]
    # return prefix_sum

    # Using in-place T.C = O(n) , S.C = O(1)
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr


arr = [1,2,3,4,5]
print(prefix_sum(arr))
arr = [1,2,3,4,5,6]
print(prefix_sum(arr))