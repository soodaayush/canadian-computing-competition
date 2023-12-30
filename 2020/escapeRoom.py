rows = int(input())
columns = int(input())

rowsArr = []

for i in range(columns):
    row = input()
    row = row.split(" ")
    rowsArr.append(row)

rowsArr.pop(len(rowsArr) - 1)

room = [[0] * columns for _ in range(rows)]

for index, element in enumerate(room):
    room[index] = rowsArr[index]

print(room)

