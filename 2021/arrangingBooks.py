unsortedBooks = "LLSLMSLSM"
unsortedBooks = list(unsortedBooks)
sortedBooks = list(unsortedBooks)

swaps = 0

sortedBooks.sort()

if sortedBooks == unsortedBooks:
    print(swaps)
else:
    for i, element in enumerate(unsortedBooks):
        for j, element2 in enumerate(unsortedBooks):
            if unsortedBooks[j] == "S" and unsortedBooks[j + 1] == "M":
                temp = unsortedBooks[j]
                unsortedBooks[j] = unsortedBooks[j + 1]
                unsortedBooks[j + 1] = temp
            if unsortedBooks[j] == "S" and unsortedBooks[j + 1] == "L":
                temp = unsortedBooks[j]
                unsortedBooks[j] = unsortedBooks[j + 1]
                unsortedBooks[j + 1] = temp
            if unsortedBooks[j] == "M" and unsortedBooks[j + 1] == "L":
                temp = unsortedBooks[j]
                unsortedBooks[j] = unsortedBooks[j + 1]
                unsortedBooks[j + 1] = temp

print(unsortedBooks)
