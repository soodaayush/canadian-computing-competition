M = int(input())
N = int(input())
K = int(input())

canvasRows, canvasCols = N, M
gCount = 0

canvas = [["B"] * canvasRows for _ in range(canvasCols)]

for i in range(K):
    choice = input().split(" ")

    if choice[0] == "R":
        for index, el in enumerate(canvas[int(choice[1]) - 1]):
            if canvas[int(choice[1]) - 1][index] == "B":
                canvas[int(choice[1]) - 1][index] = "G"
                gCount += 1
            elif canvas[int(choice[1]) - 1][index] == "G":
                canvas[int(choice[1]) - 1][index] = "B"
                gCount -= 1
    if choice[0] == "C":
        for index, el in enumerate(canvas):
            if canvas[index][int(choice[1]) - 1] == "B":
                canvas[index][int(choice[1]) - 1] = "G"
                gCount += 1
                continue
            if canvas[index][int(choice[1]) - 1] == "G":
                canvas[index][int(choice[1]) - 1] = "B"
                gCount -= 1
                continue

print(gCount)

