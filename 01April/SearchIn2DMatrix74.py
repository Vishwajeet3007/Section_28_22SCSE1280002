def searchIna2Dmatrix(matrix,target):
    # T.C: = O(m+n)
    if not matrix:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target :
            col -= 1
        else:
            row += 1
    return False
# T.C: O(m*n)
    # for i in matrix:
    #     if target in i:
    #         return True
    # return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
print(searchIna2Dmatrix(matrix,target))


