def setMatrixZeros(matrix):
    firstRow , firstCol = False , False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i == 0:
                    firstRow = True
                if j == 0 :
                    firstCol = True
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if firstRow:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0
    if firstCol:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    return matrix

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == 0:
    #             for k in range(len(matrix[0])):
    #                 if matrix[i][k] != 0:
    #                     matrix[i][k] = -1
    #             for k in range(len(matrix)):
    #                 if matrix[k][j] != 0:
    #                     matrix[k][j] = -1
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == -1:
    #             matrix[i][j] = 0
    # return matrix

matrix = [[1,1,1],[1,0,1],[1,1,2]]
print(setMatrixZeros(matrix))
