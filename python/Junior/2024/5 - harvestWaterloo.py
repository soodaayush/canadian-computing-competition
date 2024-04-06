def harvest_value(patch, startingRow, startingColumn):
    visited = set()
    totalValue = 0

    def findPumpkin(row, col):
        nonlocal totalValue

        if (
                0 <= row < len(patch)
                and 0 <= col < len(patch[0])
                and (row, col) not in visited
                and patch[row][col] in ['S', 'M', 'L']
        ):
            visited.add((row, col))

            if patch[row][col] == 'S':
                totalValue += 1
            elif patch[row][col] == 'M':
                totalValue += 5
            elif patch[row][col] == 'L':
                totalValue += 10

            findPumpkin(row + 1, col)
            findPumpkin(row - 1, col)
            findPumpkin(row, col + 1)
            findPumpkin(row, col - 1)

    findPumpkin(startingRow, startingColumn)
    return totalValue


patchArr = []

rows = int(input())
columns = int(input())

for i in range(rows):
    patchArr.append(input())

startRow = int(input())
startCol = int(input())

result = harvest_value(patchArr, startRow, startCol)
print(result)
