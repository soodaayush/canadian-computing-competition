word = list(input())

consonant = "bcdfghjklmnpqrstvwxyz"
nextConsonant = "cdfghjklmnpqrstvwxyzz"
nearestVowel = "aaeeeiiiiooooouuuuuuu"

for index, element in enumerate(word):
    if element in consonant:
        position = consonant.index(element)
        word[index] = word[index] + nearestVowel[position] + nextConsonant[position]
    elif element in nearestVowel:
        pass

print("".join(word))

