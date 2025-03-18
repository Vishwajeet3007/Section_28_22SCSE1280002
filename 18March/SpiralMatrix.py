def spiralMatrix(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    top,bottom = 0 , len(matrix)-1
    left,right = 0,len(matrix[0])-1
    while left <= right and top <= right:
        # Traverse from left to right
        for i in range(left,right + 1):
            result.append(matrix[top][i])
        top += 1

        # traverse from top to bottom
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right -= 1

        # traverse from right to left
        for i in range(right,left-1,-1):
            result.append(matrix[bottom][i])
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        left += 1
    return result
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))

