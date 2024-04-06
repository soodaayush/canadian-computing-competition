n = int(input())
yesterday = list(str(input()))
today = list(str(input()))

occupied = 0

for index, element in enumerate(yesterday):
    if yesterday[index] == "C":
        if yesterday[index] == today[index]:
            occupied = occupied + 1
    else:
        continue

print(occupied)