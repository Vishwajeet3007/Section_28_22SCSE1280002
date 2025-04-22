def find_max_xor_of_two_numbers(arr):
    max_xor = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            xor = arr[i] ^ arr[j]
            max_xor = max(max_xor,xor)
    return max_xor
nums = [3,10,5,25,2,8]
print(find_max_xor_of_two_numbers(nums))
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
print(find_max_xor_of_two_numbers(nums))