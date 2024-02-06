numOfColumns = int(input())
firstRow = input().split(" ")
secondRow = input().split(" ")

tape = 0

for index, el in enumerate(firstRow):
    if index == len(firstRow) - 1:
        if firstRow[index] == "1" and firstRow[index - 1] == "1":
            break
        elif firstRow[index] == "1" and firstRow[index - 1] != "1":
            tape += 3
            break

    if firstRow[index] == "1" and firstRow[index + 1] == "1":
        tape += 4
    elif firstRow[index] == "1" and firstRow[index + 1] != "1":
        tape += 3

print(tape)