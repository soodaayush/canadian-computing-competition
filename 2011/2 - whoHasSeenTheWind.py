humidity = int(input())
maximumTime = int(input())

hour = -1

for i in range(1, maximumTime):
    equation = (-6 * i ** 4) + (humidity * i ** 3) + (2 * i ** 2) + i

    if equation <= 0:
        hour = i
        break

if hour != -1:
    print("The balloon first touches ground at hour:" + "\n" + str(hour))
else:
    print("The balloon does not touch ground in the given time.")
