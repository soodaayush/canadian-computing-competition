firstKeys = list(str(input()))
secondKeys = list(str(input()))

indices = []

correspondingSillyKey = ""
sillyKey = ""
quietKey = "-"

if len(firstKeys) != len(secondKeys):
    for i, el in enumerate(firstKeys):
        if i < len(secondKeys):
            if firstKeys[i] != secondKeys[i] and (secondKeys[i] == firstKeys[i + 1] or i >= len(secondKeys)):
                quietKey = firstKeys[i]
                break
        else:
            quietKey = firstKeys[i]
            break

if quietKey != "-":
    for i, el in enumerate(firstKeys):
        if el == quietKey:
            indices.append(i)

    for i in indices:
        secondKeys.insert(i, quietKey)

for i, el in enumerate(secondKeys):
    if firstKeys[i] != secondKeys[i] and firstKeys[i] != quietKey:
        correspondingSillyKey = firstKeys[i]
        sillyKey = secondKeys[i]
        break

print(correspondingSillyKey + " " + sillyKey + "\n" + quietKey)
