rollCount = int(input())

rolls = []

antoniaScore = 100
davidScore = 100

for i in range(rollCount):
    rolls.append(input().split(" "))

for i in rolls:
    if i[0] < i[1]:
        antoniaScore = antoniaScore - int(i[1])
    elif i[0] > i[1]:
        davidScore = davidScore - int(i[0])
    elif i[0] == i[1]:
        pass

print(str(antoniaScore) + "\n" + str(davidScore))
