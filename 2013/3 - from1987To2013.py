year = int(input())

yearList = 0

if year == 0:
    yearList = list(range(year + 1, year + 1 * 1000))
else:
    yearList = list(range(year + 1, year * 1000))

nextUniqueYear = 0

for i in yearList:
    if len(set(str(i))) == len(str(i)):
        nextUniqueYear = i
        break

print(nextUniqueYear)