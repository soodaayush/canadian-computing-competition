M = int(input())
N = int(input())
K = int(input())

choices = []
canvasRows, canvasCols = N, M

canvas = [["B"] * canvasRows for _ in range(canvasCols)]
print(canvas)

for i in range(K):
    choice = str(input())
    choices.append(choice)

print(M, N, choices)