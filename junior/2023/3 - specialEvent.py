numberOfPeople = int(input())

attendanceList = []
attendanceObj = {}

for i in range(numberOfPeople):
    attendanceList.append([*input()])

for i in attendanceList:
    for index, j in enumerate(i):
        if index + 1 not in attendanceObj:
            attendanceObj[index + 1] = 0

        if j == "Y":
            attendanceObj[index + 1] += 1

maxValue = max(attendanceObj.values())

days = [k for k, v in attendanceObj.items() if v == maxValue]

for i, el in enumerate(days):
    days[i] = str(days[i])

print(",".join(days))

