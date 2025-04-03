def searchIna2Dmatrix(matrix,target):
    # T.C: = O(mlogn)
    for row in matrix:
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left ) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    
    return False
    
# T.C: O(m*n)
    # for i in matrix:
    #     if target in i:
    #         return True
    # return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
print(searchIna2Dmatrix(matrix,target))


