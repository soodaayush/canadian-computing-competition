# unsortedBooks = "LLSLM"
unsortedBooks = str(input())
unsortedBooksList = list(unsortedBooks)

unsortedBooks = unsortedBooks.replace("L", "3")
unsortedBooks = unsortedBooks.replace("M", "2")
unsortedBooks = unsortedBooks.replace("S", "1")

unsortedBooks = list(unsortedBooks)

sortedBooks = list(unsortedBooksList)
sortedBooks.sort()

swaps = 0
length = len(unsortedBooks) - 1

if sortedBooks == unsortedBooksList:
    print(0)
else:
    for j in range(0, length):
        if unsortedBooks[j] == "3" and unsortedBooks[j - 1] != "3":
            unsortedBooks.pop(j)
            unsortedBooks.insert(0, "3")
            swaps = swaps + 1
        elif unsortedBooks[j] == "1" and unsortedBooks[j + 1] != "1":
            unsortedBooks.pop(j)
            unsortedBooks.append("1")
            swaps = swaps + 1

    print(swaps)

