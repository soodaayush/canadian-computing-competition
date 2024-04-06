messageCount = int(input())

messages = []
received = []
sent = []
times = []

time = 0
difference = 0
sender = 0

for i in range(messageCount):
    messages.append(input().split(" "))

for index, element in enumerate(messages):
    if element[0] == "W":
        time += int(element[1])
    if element[0] == "R":
        if index == 0:
            time += 0
        elif messages[index - 1][0] == "W":
            time += 0
        else:
            time += 1
        received.append([int(element[1]), time])
    if element[0] == "S":
        if index == 0:
            time += 0
        elif messages[index - 1][0] == "W":
            time += 0
        else:
            time += 1
        sent.append([int(element[1]), time])


for index, element in enumerate(received):
    difference = 0

    for indexj, j in enumerate(sent):
        if element[0] == sent[indexj][0]:
            sender = element[0]
            if difference == 0:
                difference = sent[indexj][1] - element[1]
                sent.pop(indexj)
            else:
                difference = difference - sent[indexj][1]
                sent.pop(indexj)

    times.append([element[0], difference])

for indexi, i in enumerate(times):
    for indexj, j in enumerate(times[indexi + 1:]):
        if i[0] == j[0]:
            i[1] = i[1] + j[1]
            times.pop(indexj)

    print(*i, sep=" ")
