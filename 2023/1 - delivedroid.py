p = int(input())
c = int(input())

points = (p * 50) - (c * 10)

if p > c:
    points += 500
    print(points)
else:
    print(points)