import math

inputMinutes = int(input())

favoriteTimes = []

# hours = 12
# minutes = 0
# totalTimeDistance = 0
#
hoursSince12 = 0
minutesSince12 = 0
#
# if inputMinutes >= 60:
#     hoursSince12 = math.floor(inputMinutes / 60)
#     minutesSince12 = inputMinutes % 60
# else:
#     hoursSince12 = 12
#     minutesSince12 = inputMinutes
#
# if minutesSince12 == 0:
#     totalTimeDistance = str(hoursSince12) + "00"
# elif minutesSince12 < 10:
#     totalTimeDistance = str(hoursSince12) + "0" + str(minutesSince12)
# elif minutesSince12 >= 10:
#     totalTimeDistance = str(hoursSince12) + str(minutesSince12)
#
# print(totalTimeDistance)
#
# # ranges = list(range(1200, int(totalTimeDistance) + 1))

# print(ranges)

if inputMinutes >= 60:
    hoursSince12 = math.floor(inputMinutes / 60)
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

# for i in range(1000):
#     if hours == 12 and minutes >= 34:
#         favoriteTimes.append("12:34")
#         hours = 1
#     if hours == 1:
#         favoriteTimes.append("1:11")
#         favoriteTimes.append("1:23")
#         favoriteTimes.append("1:35")
#         favoriteTimes.append("1:47")
#         favoriteTimes.append("1:59")
#     if hours == 2:
#         favoriteTimes.append()


