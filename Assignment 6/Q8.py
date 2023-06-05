def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for x in range(k):
                if mat1[i][x] != 0 and mat2[x][j] != 0:
                    result[i][j] += mat1[i][x] * mat2[x][j]

    return result

mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(multiply(mat1, mat2))  # Output: [[7, 0, 0], [-7, 0, 3]]