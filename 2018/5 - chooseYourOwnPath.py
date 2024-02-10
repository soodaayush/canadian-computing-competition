pages = int(input())

options = []

pageRange = set(range(1, pages + 1))
numSet = set()
numSet.add(1)
reachable = ""
deadEnds = []

for i in range(pages):
    options.append(input().split(" "))

for i in options:
    for j in i:
        numSet.add(int(j))

if 0 in numSet:
    numSet.remove(0)

numSet = sorted(numSet)

if set(numSet) == pageRange:
    reachable = "Y"
else:
    reachable = "N"

for index, element in enumerate(options):
    if element == ["0"]:
        deadEnds.append(index + 1)

print(deadEnds)

print(reachable + "\n" + str(min(deadEnds)))
