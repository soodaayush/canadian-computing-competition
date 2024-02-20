instructions = str(input())
instructionsList = list(instructions)

grid = [[1, 2], [3, 4]]

for i in instructionsList:
    if i == "H":
        grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
        grid[0][1], grid[1][1] = grid[1][1], grid[0][1]
    elif i == "V":
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

print(str(grid[0][0]) + " " + str(grid[0][1]) + "\n" + str(grid[1][0]) + " " + str(grid[1][1]))
