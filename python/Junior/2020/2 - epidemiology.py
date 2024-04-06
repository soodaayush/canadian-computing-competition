p = int(input())
n = int(input())
r = int(input())

infected = n
infectedTotal = n
day = 0


for i in range(1000000000000000000000):
    if infectedTotal > p:
        print(day)
        break

    infected = infected * r
    infectedTotal += infected
    day += 1
