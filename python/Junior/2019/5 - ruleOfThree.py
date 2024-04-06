# firstRule = str(input()).split(" ")
firstRule = "AA AB".split(" ")
# secondRule = str(input()).split(" ")
secondRule = "AB BB".split(" ")
# thirdRule = str(input()).split(" ")
thirdRule = "B AA".split(" ")
# letters = str(input()).split(" ")
letters = "4 AB AAAB".split(" ")

steps = letters[0]
startingPoint = letters[1]
endPoint = letters[2]

stepCount = 0

for i in range(int(steps)):
    if firstRule[0] in startingPoint:
        startingPoint = startingPoint.replace(firstRule[0], firstRule[1], 1)
        continue
    elif secondRule[0] in startingPoint:
        startingPoint = startingPoint.replace(secondRule[0], secondRule[1], 1)
        continue
    if thirdRule[0] in startingPoint:
        startingPoint = startingPoint.replace(thirdRule[0], thirdRule[1], 1)
        continue

print(startingPoint)