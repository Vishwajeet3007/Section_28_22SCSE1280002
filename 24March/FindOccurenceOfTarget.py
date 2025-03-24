from collections import Counter
def findOccureceOfTarget(arr,target):
    freq = Counter(arr)
    return freq[target]
arr = [1,2,2,2,3,4,5]
target =  2
print(findOccureceOfTarget(arr,target)) 

def findOccurence(arr,target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count
arr = [1,2,2,2,2,3,4,5]
target = 2
print(findOccurence(arr,target))