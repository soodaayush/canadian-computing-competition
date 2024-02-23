scoreCount = int(input())

scores = []

for i in range(scoreCount):
    scores.append(int(input()))

scoresSet = set(scores)
scoresSet = list(reversed(sorted(scoresSet)))

print(scoresSet[2], scores.count(scoresSet[2]))