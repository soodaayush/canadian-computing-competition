unsortedBooks = "LLSLMSLSM"
unsortedBooks = unsortedBooks.replace("L", "3")
unsortedBooks = unsortedBooks.replace("M", "2")
unsortedBooks = unsortedBooks.replace("S", "1")
unsortedBooks = list(unsortedBooks)
sortedBooks = list(unsortedBooks)

swaps = 0

sortedBooks.sort(reverse=True)

if sortedBooks == unsortedBooks:
    print(swaps)
else:
    for i in range(0, len(unsortedBooks) - 1):
        for j in range(0, len(unsortedBooks) - 1):
            if unsortedBooks[j] < unsortedBooks[j + 1]:
                temp = unsortedBooks[j]
                unsortedBooks[j] = unsortedBooks[j + 1]
                unsortedBooks[j + 1] = temp
                swaps = swaps + 1
    if sortedBooks == unsortedBooks:
        print(swaps)

