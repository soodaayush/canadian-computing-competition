# Problem 1

def cupcakeParty(r, s):
    regular = 8 * r
    small = 3 * s
    total = regular + small

    return total - 28


print(cupcakeParty(2, 3))


# Problem 2

def fergusonBallRatings(n, players):
    scores = []

    for i in players:
        scores.append(i[0] * 5 - i[1] * 3)

    if min(scores) > 40:
        return f"{len(scores)}+"
    else:
        return len([1 for i in scores if i > 40])


print(fergusonBallRatings(2, [[8, 0], [12, 1]]))


# Problem 3

def harpTuning(instructions):
    instruction = ""
    cleanInstructions = []

    for i in instructions:
        if i == "+":
            instruction += " tighten "

        if i == "-":
            instruction += " loosen "

        if i.isnumeric():
            instruction += i
            cleanInstructions.append(instruction)
            instruction = ""
        elif i != "+" and i != "-":
            instruction += i

    return cleanInstructions


print(harpTuning("AFB+8SC-4H-2GDPE+9"))


# Problem 4

def goodGroups(x, sameGroup, y, notSameGroup, g, groups):
    print("Yay!")


print(goodGroups(1, ["ELODIE", "CHI"], 0, 0, 2, [["DWAYNE", "BEN", "ANJALI"], ["CHI", "FRANCOIS", "ELODIE"]]))
