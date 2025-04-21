def find_two_numbers(arr,target):
    #USing Two Pointers  T.C = O(n) and S.C = O(1)

    # left = 0
    # right = len(arr) - 1
    # while left < right:
    #     curr_sum = arr[left] + arr[right]
    #     if curr_sum == target:
    #         return arr[left],arr[right]
    #     elif curr_sum  < target:
    #         left += 1
    #     else:
    #         right -= 1
    # return 'No Pair Found'

# Using Brute Force  T.C = O(n*n) and S.C = O(1)
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return arr[i] , arr[j]
    return 'No Pair Found'


arr = 1,3,4,5,7,10,11
target = 9
print(find_two_numbers(arr,target))