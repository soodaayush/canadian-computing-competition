def fergusonBallRatings(n, players):
    scores = []

    for i in players:
        scores.append(i[0] * 5 - i[1] * 3)

    if min(scores) > 40:
        return f"{len(scores)}+"
    else:
        return len([1 for i in scores if i > 40])


# print(fergusonBallRatings(3, [[12, 4], [10, 3], [9, 1]]))