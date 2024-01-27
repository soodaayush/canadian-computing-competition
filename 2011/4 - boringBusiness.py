plan = [
    [0, -1],
    [0, -2],
    [0, -3],
    [1, -3],
    [2, -3],
    [3, -3],
    [3, -4],
    [3, -5],
    [4, -5],
    [5, -5],
    [5, -4],
    [5, -3],
    [6, -3],
    [7, -3],
    [7, -4],
    [7, -5],
    [7, -6],
    [7, -7],
    [6, -7],
    [5, -7],
    [4, -7],
    [3, -7],
    [2, -7],
    [1, -7],
    [0, -7],
    [-1, -7],
    [-1, -6],
    [-1, -5]
]

cols = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rows = [-1, -2, -3, -4, -5, -6, -7, -8]

startingPosition = [-1, -5]
directionArr = []
directions = []

maxCols = 14
maxRows = 8

while True:
    i = input().split(" ")
    directionArr.append(i)
    if i[0] == "q":
        break
    if i[0] == "":
        directionArr.pop()
        break

for i in directionArr:
    direction = i[0]
    directionCount = int(i[1])
    safe = "safe"

    if direction == "q":
        break
    while directionCount > 0:
        if direction == "l":
            startingPosition[0] -= 1
        elif direction == "r":
            startingPosition[0] += 1
        elif direction == "u":
            startingPosition[1] += 1
        elif direction == "d":
            startingPosition[1] -= 1
        directionCount -= 1

        if startingPosition in plan or (startingPosition[0] not in cols) or (startingPosition[1] not in rows):
            safe = "DANGER"
        else:
            plan.append(startingPosition.copy())

    directions.append([startingPosition[0], startingPosition[1], safe])

    if safe == "DANGER":
        break
    else:
        continue

for i in directions:
    print(*i)
