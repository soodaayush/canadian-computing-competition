sunflowerCount = int(input())

sunflowerArr = []

for i in range(sunflowerCount):
    sunflowerArr.append(input().split(" "))

smallestNum = min(int(sunflowerArr[0][0]), int(sunflowerArr[0][sunflowerCount - 1]),
                  int(sunflowerArr[sunflowerCount - 1][0]), int(sunflowerArr[sunflowerCount - 1][sunflowerCount - 1]))

# var1 = (reversed(sunflowerArr))  # Reverses list
# print(var1)  # Only prints reverseiterator object, need to convert it to list to see results
# var2 = list(zip(*var1))  # Groups all elements from the same position into tuples e.g: [[1, 2, 3], [4, 5, 6], [7, 8, 9
# # ]] -> [(1, 4, 7) (2, 5, 8), (3, 6, 9)]
# print(var2)

for i in range(10):
    if int(sunflowerArr[0][0]) != smallestNum:
        var1 = (reversed(sunflowerArr))
        sunflowerArr = list(zip(*var1))
        continue
    if int(sunflowerArr[0][0]) == smallestNum:
        break


for i in sunflowerArr:
    print(*i)
