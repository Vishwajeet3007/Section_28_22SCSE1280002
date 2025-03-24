def first_Binary_search(nums,target):
        ans=-1
        left=0
        right=len(nums)-1
        while left <= right:
            mid=(left + right)//2
            if nums[mid]==target:
                ans = mid
                right= mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left =mid + 1
        return ans
print(first_Binary_search([5,7,7,8,8,10],8))
