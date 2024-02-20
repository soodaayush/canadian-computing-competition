messageCount = int(input())

decodedMessages = []

for i in range(messageCount):
    message = input()
    message = message.split(" ")
    decodedMessages.append(message[1] * int(message[0]))

for i in decodedMessages:
    print(i)
