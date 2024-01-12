game1 = str(input())
game2 = str(input())
game3 = str(input())
game4 = str(input())
game5 = str(input())
game6 = str(input())

scores = [game1, game2, game3, game4, game5, game6]

if scores.count("W") == 5 or scores.count("W") == 6:
    print("1")
elif scores.count("W") == 3 or scores.count("W") == 4:
    print("2")
elif scores.count("W") == 1 or scores.count("W") == 2:
    print("3")
else:
    print("-1")
