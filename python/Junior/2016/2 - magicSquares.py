total = []

vertical1 = 0
vertical2 = 0
vertical3 = 0
vertical4 = 0

magic = 0

for i in range(4):
    new = input()
    line = new.split()
    horizontal = 0

    vertical1 += int(line[0])
    vertical2 += int(line[1])
    vertical3 += int(line[2])
    vertical4 += int(line[3])

    for i in range(0, len(line)):
        horizontal += int(line[i])
    total.append(horizontal)

total.append(vertical1)
total.append(vertical2)
total.append(vertical3)
total.append(vertical4)

for i in range(len(total)):
    if total[0] != total[i]:
        magic += 1

if magic == 0:
    print("magic")
else:
    print("not magic")