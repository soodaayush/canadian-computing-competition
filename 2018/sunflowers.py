sunflowerCount = int(input())

sunflowerArr = []

for i in range(sunflowerCount):
    sunflowerArr.append(input().split(" "))

smallestNum = min(int(sunflowerArr[0][0]), int(sunflowerArr[0][sunflowerCount - 1]), int(sunflowerArr[sunflowerCount - 1][0]), int(sunflowerArr[sunflowerCount - 1][sunflowerCount - 1]))

for i in range(10):
    if int(sunflowerArr[0][0]) != smallestNum:
        var1 = (reversed(sunflowerArr))
        sunflowerArr = list(zip(*var1))
        continue
    if int(sunflowerArr[0][0]) == smallestNum:
        break


for i in sunflowerArr:
    print(*i)
