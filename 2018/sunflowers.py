sunflowerCount = int(input())

sunflowerArr = []

for i in range(sunflowerCount):
    sunflowerArr.append(input().split(" "))


def rotate90():
    for j in range(sunflowerCount):
        for i in range(sunflowerCount - 1, -1, -1):
            print(sunflowerArr[i][j], end=" ")
        print()


for i in sunflowerArr:
    if sorted(i) != i:
        rotate90()

print(sunflowerArr)