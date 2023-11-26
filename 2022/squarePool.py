def find_largest_square(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_size = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:  # Unoccupied element
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                max_size = max(max_size, dp[i][j])

    return max_size

# Example usage
matrix = [
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0]
]

result = find_largest_square(matrix)
print("Largest square block size:", result)
