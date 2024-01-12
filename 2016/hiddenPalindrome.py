word = input()
length = []

letterToLetter = 0

for i in range(len(word)):
    for j in range(i, len(word)):
        letterToLetter = word[i:j + 1]
        if letterToLetter == letterToLetter[::-1]:
            length.append(len(letterToLetter))

print(max(length))
