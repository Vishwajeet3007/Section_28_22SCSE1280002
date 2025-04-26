def nextPermutation(nums):
    # Pivot == gola_index
    
    n = len(nums)
    gola_index = -1

    # Step 1 : finding first decreasing element from the end side
    for i in range(n-1,0,-1):
        if nums[i] > nums[i - 1]:
            gola_index = i - 1
            break 
    # Step 2 : If element found ,swap it with just larger number
    if gola_index != -1:
        for j in range(n-1,gola_index,-1):
            if nums[j] > nums[gola_index]:
                nums[gola_index] , nums[j] = nums[j] , nums[gola_index]
                break
    # Reverse the suffix part
    nums[gola_index + 1 : ] = reversed(nums[gola_index + 1:])
nums = [2,1,3]
nextPermutation(nums)
print(nums)
