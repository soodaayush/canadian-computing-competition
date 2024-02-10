compressCount = int(input())

compressed = []
encodedMessages = []

for i in range(compressCount):
    compressed.append(list(input()))

for j in range(compressCount):
    count = 0
    message = ""
    messageArr = compressed[j]

    for i in range(len(messageArr)):
        if i != len(messageArr) - 1 and messageArr[i] == messageArr[i + 1]:
            count = count + 1
        else:
            message = message + " " + str(count + 1) + " " + messageArr[i]
            encodedMessage = message
            count = 0

    print(encodedMessage)