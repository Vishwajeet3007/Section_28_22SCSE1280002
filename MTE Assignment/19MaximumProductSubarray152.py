def max_product_Subarray(nums):
    # # Brute Force T.C = O(n*n)  S.C = O(1)
    # n = len(nums)
    # max_product = nums[0]
    # for i in range(n):
    #     product = 1
    #     for j in range(i,n):
    #         product *= nums[j]
    #         max_product = max(max_product,product)
    # return max_product

     # Using Optimal T.C = O(n) S.C=O(1)
    if not nums:
        return 0
    max_so_far = min_so_far = max_product = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        if num < 0:
           max_so_far,min_so_far=min_so_far,max_so_far
        max_so_far = max(num , max_so_far * num)
        min_so_far = min(num , min_so_far * num)
        max_product = max(max_product , max_so_far)
    return max_product
          
nums = [2,3,-2,4]
print(max_product_Subarray(nums))
nums = [-2,0,-1]
print(max_product_Subarray(nums))