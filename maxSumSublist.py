def max_sum_sublist(arr,k):
    # arr.sort(reverse = True)
    # max_sum = sum(arr[:k])
    
    max_sum=curr_sum = sum(arr[:k])
    for i in range(k,len(arr)):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum,curr_sum)
    return max_sum
arr = [10,15,20,25,5]
k = 2
print(max_sum_sublist(arr, k)) 
