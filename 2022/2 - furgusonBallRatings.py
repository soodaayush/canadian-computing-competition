players = int(input())
count = 0
isGold = ""

for i in range(players):
    scores = int(input())
    fouls = int(input())
    pts = (5 * scores) - (3 * fouls)
    if pts > 40:
        count += 1

if count == players:
    isGold = "+"

print(str(count)+isGold)
