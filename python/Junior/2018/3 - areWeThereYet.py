distances = str(input()).split(" ")

city1 = 0
city2 = int(distances[0])
city3 = int(distances[1])
city4 = int(distances[2])
city5 = int(distances[3])

distanceArr = []

for i in range(1):
    distanceArr.append([city1, city2, city2 + city3, city2 + city3 + city4, city2 + city3 + city4 + city5])
    distanceArr.append([city2, city1, city3, city3 + city4, city3 + city4 + city5])
    distanceArr.append([city2 + city3, city3, city1, city4, city4 + city5])
    distanceArr.append([city2 + city3 + city4, city3 + city4, city4, city1, city5])
    distanceArr.append([city2 + city3 + city4 + city5, city3 + city4 + city5, city4 + city5, city5, city1])

for i in distanceArr:
    print(*i)


