def squarePool(n, t, trees):
    matrixRows, matrixCols = n, n
    matrix = [[0] * matrixRows for _ in range(matrixCols)]

    for index, i in enumerate(trees):
        matrix[trees[index][0]][trees[index][1] - 1] = 1

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_size = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:  # Unoccupied element
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_size = max(max_size, dp[i][j])

    return max_size


print(squarePool(15, 8, [[4, 7], [4, 1], [14, 11], [10, 6], [13, 4], [4, 10], [10, 3], [9, 14]]))
