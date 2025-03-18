def EquilibriumIndex(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i,num in enumerate(arr):
        if left_sum == total_sum -left_sum - num:
            return i
        left_sum += num
    return -1
arr= [-7,1,5,2,-4,3,0]
result = EquilibriumIndex(arr)
print(result)