def devlivedroid(p, c):
    delivered = p * 50
    collisions = c * 10

    points = delivered - collisions

    if p > c:
        points = points + 500

    return points


print(devlivedroid(0, 10))