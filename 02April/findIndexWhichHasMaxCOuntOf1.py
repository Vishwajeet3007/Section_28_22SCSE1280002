def count1(matrix):
    
    idx = -1
    result = 0
    for row in range(len(matrix)):
        count = matrix[row].count(1)
        if count > result:
            result = count
            idx = row
    return idx
matrix = [[0,0,0],[0,0,1],[1,1,1]]
print(count1(matrix))
            
