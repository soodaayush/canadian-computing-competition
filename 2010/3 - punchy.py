import sys

a = 0
b = 0

while True:
    i = input().split(" ")

    if i[0] == "7":
        sys.exit()

    if i[0] == "1":
        if i[1] == "A":
            a = int(i[2])
        elif i[1] == "B":
            b = int(i[2])
    if i[0] == "2":
        if i[1] == "A":
            print(a)
        elif i[1] == "B":
            print(b)
    if i[0] == "3":
        if i[1] == "A" and i[2] == "A":
            a = a + a
        elif i[1] == "A" and i[2] == "B":
            a = a + b
        elif i[1] == "B" and i[2] == "A":
            b = b + a
        elif i[1] == "B" and i[2] == "B":
            b = b + b
    if i[0] == "4":
        if i[1] == "A" and i[2] == "A":
            a = a * a
        elif i[1] == "A" and i[2] == "B":
            a = a * b
        elif i[1] == "B" and i[2] == "A":
            b = b * a
        elif i[1] == "B" and i[2] == "B":
            b = b * b
    if i[0] == "5":
        if i[1] == "A" and i[2] == "A":
            a = a - a
        elif i[1] == "A" and i[2] == "B":
            a = a - b
        elif i[1] == "B" and i[2] == "A":
            b = b - a
        elif i[1] == "B" and i[2] == "B":
            b = b - b
    if i[0] == "6":
        if i[1] == "A" and i[2] == "A":
            a = a // a
        elif i[1] == "A" and i[2] == "B":
            a = a // b
        elif i[1] == "B" and i[2] == "A":
            b = b // a
        elif i[1] == "B" and i[2] == "B":
            b = b // b
