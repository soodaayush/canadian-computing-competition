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