def nextGreaterElement1(arr):
    result = [-1] * len(arr)
    # USing Brute Force
    # for i in range(len(arr)-1):
    #     for j in range(i+1,len(arr)):
    #         if arr[i] < arr[j]:
    #             result[i] = arr[j]
    #             break

    # USing Stack 
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result
            
    # return result
arr = [6,0,8,1,3]
print(nextGreaterElement1(arr))
arr = [4,12,5,3,1,2,5,3,1,2,4,6]
print(nextGreaterElement1(arr))
