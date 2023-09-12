# Problem 1

def devlivedroid(p, c):
    delivered = p * 50
    collisions = c * 10

    points = delivered - collisions

    if p > c:
        points = points + 500

    return points


print(devlivedroid(0, 10))


# Problem 2

def chiliPeppers(n, list):
    peppers = {
        "poblano": 1500,
        "mirasol": 6000,
        "serrano": 15500,
        "cayenne": 40000,
        "thai": 75000,
        "habanero": 125000
    }

    spice = 0

    for i in list:
        spice += peppers[i.lower()]

    return spice


print(chiliPeppers(4, ["Poblano", "Cayenne", "Thai", "Poblano"]))


# Problem 3

def specialEvent(people, list):
    days = []
    result = []

    for i in list:
        days.append(i.count("Y"))

    day = max(days)

    for index, item in enumerate(days):
        if item == day:
            result.append(index + 1)

    return result


print(specialEvent(3, [["Y", ".", ".", ".", "Y"], ["Y", "Y", "Y", "Y", "."], [".", "Y", ".", "Y", "."],
                       [".", ".", "Y", ".", "."], ["Y", "Y", ".", "Y", "Y"]]))


# Problem 4

def trianglane(c, lanes):
    length = 0
    nextLane = []
    lastLane = []

    for arrIndex, item in enumerate(lanes):
        if arrIndex != len(lanes) - 1:
            nextLane = lanes[arrIndex + 1]

        if arrIndex != 0:
            lastLane = lanes[arrIndex - 1]

        if item.count(1) == 2 and nextLane[0] == 1:
            length += 5
            continue

        if item[0] == 1 and lastLane.count(1) == 2:
            length += 0
            continue

        if item.count(1) == 1:
            length += 3
            continue

    return length


print(trianglane(7, [[0, 0], [0, 0], [1, 1], [1, 0], [0, 1], [1, 0], [0, 0]]))

# Problem 5
