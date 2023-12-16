unsortedBooks = str(input())
unsortedBooks = unsortedBooks.replace("L", "3")
unsortedBooks = unsortedBooks.replace("M", "2")
unsortedBooks = unsortedBooks.replace("S", "1")

unsortedBooks = list(unsortedBooks)
sortedBooks = list(unsortedBooks)

swaps = 0

sortedBooks.sort()

if sortedBooks == unsortedBooks:
    print(swaps)

for index, element in enumerate(unsortedBooks):
    if index == 0:
        if int(unsortedBooks[index]) < int(unsortedBooks[index + 1]):
            unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
            swaps = swaps + 1
    elif index == len(unsortedBooks) - 1:
        if int(unsortedBooks[index]) > int(unsortedBooks[index - 1]):
            unsortedBooks[index - 1], unsortedBooks[index] = unsortedBooks[index], unsortedBooks[index - 1]
            swaps = swaps + 1
    elif int(unsortedBooks[index]) < int(unsortedBooks[index + 1]) and int(unsortedBooks[index]) < int(unsortedBooks[index - 1]):
        unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
        swaps = swaps + 1

print(swaps)



