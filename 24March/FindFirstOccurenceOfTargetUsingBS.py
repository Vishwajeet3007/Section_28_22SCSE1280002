def first_Binary_search(nums,target):
        ans=-1
        left=0
        right=len(nums)-1
        mid = left + (right - left)// 2
        while left <= right:
            
            if nums[mid]==target:
                ans = mid
                right= mid - 1
          
            if nums[mid] > target:
                right = mid - 1
            else:
                left =mid + 1
            mid = left + (right - left)//2
        return ans-1
print(first_Binary_search([5,7,7,8,8,10],8))
