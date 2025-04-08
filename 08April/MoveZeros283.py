def moveZeros(nums):
#    T.C=S.C=O(n)
    # new_num = []
    # for num in nums:
    #     if num != 0:
    #         new_num.append(num)
    # new_num += [0] * (len(nums)-len(new_num))
    # return new_num

    # T.c = O(n) and S.c= O(1)
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1
    for i in range(insert_pos,len(nums)):
        nums[i] = 0
    return nums
nums = [0,12,2,0,3,12]
print(moveZeros(nums))