coordinates = int(input())

x = []
y = []

for i in range(coordinates):
    coordinate = str(input())
    xAndY = coordinate.split(",")
    x.append(xAndY[0])
    y.append(xAndY[1])

bottomLeftX = int(min(x)) - 1
bottomLeftY = int(min(y)) - 1
topRightX = int(max(x)) + 1
topRightY = int(max(y)) + 1

print(str(bottomLeftX) + "," + str(bottomLeftY) + "\n" + str(topRightX) + "," + str(topRightY))
