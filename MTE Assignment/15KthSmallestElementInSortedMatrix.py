def KthSmallest(matrix,k):
    flat_list = []
    for row in matrix:
        for num in row:
            flat_list.append(num)
    flat_list.sort()
    return flat_list[k-1]
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8

print(KthSmallest(matrix, k)) 
