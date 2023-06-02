def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))