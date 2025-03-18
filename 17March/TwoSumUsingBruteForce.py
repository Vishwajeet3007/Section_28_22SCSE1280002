def twoSum(arr,target):
     #O(n^2)
    for i in range(len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]  
              # return True              "YES" or "NO" // i,j====> [3,4] if not present then [-1,1]
                return "YES"
    # return [-1,1]
    # return False
    return "NO"

arr = [4,6,8,4,2]
target = 14
print(twoSum(arr,target))
