def goodGroups(x, sameGroup, y, notSameGroup, g, groups):
    constraints = 0

    for sameGroupIndex, i in enumerate(sameGroup):
        for groupIndex, j in enumerate(groups):
            if all(item in j for item in i) is True:
                continue

            if all(item in j for item in i) is False and groupIndex == len(groups) - 1:
                constraints = constraints + 1

    for notSameGroupIndex, x in enumerate(notSameGroup):
        for groupIndex, y in enumerate(groups):
            if all(item in y for item in x) is False:
                continue

            if all(item in y for item in x) is True:
                constraints = constraints + 1

    return constraints


print(goodGroups(2, [["ELODIE", "CHI"],["A","B"]], 0, [], 2,
                 [["DWAYNE", "BEN", "ANJALI"], ["CHI", "A", "B","ELODIE"]]))