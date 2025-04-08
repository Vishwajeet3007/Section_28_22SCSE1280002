def fourSum( nums, target):
    #Using Brute Force T.C=O(n^4) 
    result = set()
    nums.sort()
    for i in range(len(nums)-3):
        for j in range(i+1,len(nums)-2):
            for k in range(j+1,len(nums)-1):
                for l in range(k+1,len(nums)):
                    if nums[i] + nums[j] + nums[k]+nums[l] == target:
                        result.add((nums[i],nums[j],nums[k],nums[l]))
    return list(map(list,result))
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))
nums = [2,2,2,2,2]
target = 8
print(fourSum(nums,target))

