instructionStr = ""

while True:
    num = input()

    if num == "99999":
        break

    digitsSum = int(num[0]) + int(num[1])

    if digitsSum % 2 == 1:
        instructionStr = "left "
    elif digitsSum == 0:
        pass
    else:
        instructionStr = "right "

    print(instructionStr + num[2:])




