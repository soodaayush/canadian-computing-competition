n = int(input())
k = int(input())
index = 0

if n == k:
    print(1)
elif k == 1:
    print(n)

combinations = list("1" * k)
combinationList = []

for indexi, el in enumerate(combinations):
    combinations[indexi] = int(el)

for el in range(len(combinations) * n):
    if index == len(combinations) - n - 1:
        break

    if combinations[index] == n - len(combinations) - 1:
        if sum(combinations) == n:
            combinationList.append(n)
        else:
            index += 1

    if sum(combinations) == n:
        combinationList.append(n)
    else:
        combinations[index] += 1

print(combinationList)
