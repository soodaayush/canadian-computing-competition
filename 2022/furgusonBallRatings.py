# n = int(input())
#
# players = []
# player = []
#
# for i in range(n):
#     if len(player) == 2:
#         players.append(player)
#         player = []
#
#     a = int(input())
#     player.append(a)
#
# scores = []
# print(players)
#
# for i in players:
#     scores.append(i[0] * 5 - i[1] * 3)
#
# if min(scores) > 40:
#     print(f"{len(scores)}+")
# else:
#     print(len([1 for i in scores if i > 40]))
#


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
