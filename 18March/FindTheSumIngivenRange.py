def findSumInGivenRange(arr,start,end):
    summ = 0
    for i in range(start,end + 1):
        summ += arr[i]
    return summ
arr = [1,2,3,4,5,6,7]
start = 2
end = 5
result = findSumInGivenRange(arr,start,end)
print(result)