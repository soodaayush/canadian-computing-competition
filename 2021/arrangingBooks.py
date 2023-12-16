unsortedBooks = "LLSLMSLSM"
unsortedBooks = list(unsortedBooks)
sortedBooks = list(unsortedBooks)

swaps = 0

sortedBooks.sort()

if sortedBooks == unsortedBooks:
    print(swaps)
else:
    for index, element in enumerate(unsortedBooks):
        if index == 0:
            if unsortedBooks[index] == "S" and unsortedBooks[index + 1] == "L" or unsortedBooks[index + 1] == "M":
                unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
                swaps = swaps + 1
            elif unsortedBooks[index] == "M" and unsortedBooks[index + 1] == "L" or unsortedBooks[index + 1] == "S":
                unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
                swaps = swaps + 1
        if index == len(unsortedBooks) - 1:
            if unsortedBooks[index] == "L" and unsortedBooks[index - 1] == "M":
                unsortedBooks[index - 1], unsortedBooks[index] = unsortedBooks[index], unsortedBooks[index - 1]
                swaps = swaps + 1
            if unsortedBooks[index] == "L" and unsortedBooks[index - 1] == "S":
                unsortedBooks[index - 1], unsortedBooks[index] = unsortedBooks[index], unsortedBooks[index - 1]
                swaps = swaps + 1
            if unsortedBooks[index] == "M" and unsortedBooks[index - 1] == "S":
                unsortedBooks[index - 1], unsortedBooks[index] = unsortedBooks[index], unsortedBooks[index - 1]
                swaps = swaps + 1
            break
        if unsortedBooks[index] == "S" and unsortedBooks[index + 1] == "L":
            unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
            swaps = swaps + 1
        elif unsortedBooks[index] == "S" and unsortedBooks[index + 1] == "M":
            unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
            swaps = swaps + 1
        elif unsortedBooks[index] == "M" and unsortedBooks[index + 1] == "L":
            unsortedBooks[index], unsortedBooks[index + 1] = unsortedBooks[index + 1], unsortedBooks[index]
            swaps = swaps + 1
        elif unsortedBooks[index] == "M" and unsortedBooks[index - 1] == "S":
            unsortedBooks[index - 1], unsortedBooks[index] = unsortedBooks[index], unsortedBooks[index - 1]
            swaps = swaps + 1

    if unsortedBooks == sortedBooks:
        print(swaps)
