favoriteTeam = int(input())
numberOfGamesPlayed = int(input())

games = []
gamesList = []

team1 = []
team2 = []
team3 = []
team4 = []

team1pts = 0
team2pts = 0
team3pts = 0
team4pts = 0

for i in range(numberOfGamesPlayed):
    games.append(input().split(" "))

for i in games:
    for index, el in enumerate(i):
        if index == 0:
            team1.append(el)
        if index == 1:
            team2.append(el)
        if index == 2:
            team3.append(el)
        if index == 3:
            team4.append(el)

gamesList.append(team1)
gamesList.append(team2)
gamesList.append(team3)
gamesList.append(team4)

for index, el in enumerate(team1):
    if team1[index] < team2[index]:
        team2pts += 3
    elif team1[index] > team2[index]:
        team1pts += 3
    elif team1[index] == team2[index]:
        team1pts += 1
        team2pts += 1

for index, el in enumerate(team3):
    if team3[index] < team4[index]:
        team4pts += 3
    elif team3[index] > team4[index]:
        team3pts += 3
    elif team3[index] == team4[index]:
        team3pts += 1
        team4pts += 1

print(0)

