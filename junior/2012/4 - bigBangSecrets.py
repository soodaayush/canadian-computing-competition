k = int(input())
word = list(str(input()))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

newWordPosition = 0

for index, el in enumerate(word):
    newWordPosition = 3 * (index + 1) + k
    newWordPosition = letters.index(el) - newWordPosition
    word[index] = letters[newWordPosition]

print("".join(word))
