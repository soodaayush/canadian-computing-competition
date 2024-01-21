minutes = int(input())
choreCount = int(input())
chores = []

minutesSpent = 0
choresDone = 0

for i in range(choreCount):
    chores.append(int(input()))

chores.sort()

for i in chores:
    if minutesSpent + i <= minutes:
        choresDone += 1
        minutesSpent += i
    elif minutesSpent + i > minutes:
        break

print(choresDone)
