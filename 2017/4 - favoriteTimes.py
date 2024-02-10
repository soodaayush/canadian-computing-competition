import math

inputMinutes = int(input())

favoriteTimes = []

hoursSince12 = 0
minutesSince12 = 0

if inputMinutes >= 60:
    hoursSince12 = math.floor(inputMinutes / 60)

    if hoursSince12 > 12:
        for i in range(hoursSince12):
            if hoursSince12 > 12:
                hoursSince12 = hoursSince12 % 12
            else:
                break

    minutesSince12 = inputMinutes % 60
else:
    hoursSince12 = 12
    minutesSince12 = inputMinutes

totalTimeDistance = 0

if minutesSince12 == 0:
    totalTimeDistance = str(hoursSince12) + ":" + "00"
elif minutesSince12 < 10:
    totalTimeDistance = str(hoursSince12) + ":" + "0" + str(minutesSince12)
elif minutesSince12 >= 10:
    totalTimeDistance = str(hoursSince12) + ":" + str(minutesSince12)


print(totalTimeDistance)



