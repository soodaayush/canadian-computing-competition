wordToCheck = str(input())
word = str(input())

shift = 0

word = list(word)
cycles = []
wordFound = []

for i in word:
    letter = word[0]
    word.pop(0)
    word.append(letter)
    cycles.append("".join(word))

for i in cycles:
    if wordToCheck.find(i) != -1:
        print("yes")
        wordFound.append(i)
        break

if len(wordFound) == 0:
    print("no")
