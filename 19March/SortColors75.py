from collections import Counter
def sortColors(arr):
    # i=0
    # j=0
    # k=len(arr)-1
    # while j <= k:
    #     if arr[j] == 1:
    #         j += 1
    #     elif arr[j] == 2:
    #         arr[j] ,arr[k] = arr[k] ,arr[j]
    #         k -= 1
    #     else:
    #         arr[j] , arr[i] = arr[i] , arr[j]
    #         j += 1
    #         i += 1
    # return arr

    count0 = 0
    count1 =  0
    count2 = 0 
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    index = 0
    for _ in range(count0):
        arr[index] = 0
        index += 1
    for _ in range(count1):
        arr[index] = 1
        index += 1
    for _ in range(count2):
        arr[index] = 2
        index += 1
        
    return arr


arr = [0,2,1,0,2]
print(sortColors(arr)) 