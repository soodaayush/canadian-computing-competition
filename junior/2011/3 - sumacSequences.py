firstNumber = int(input())
secondNumber = int(input())

sumacArr = [firstNumber, secondNumber]

index = 2

for i in range(secondNumber):
    nextNum = sumacArr[index - 2] - sumacArr[index - 1]

    if nextNum < 0:
        break
    else:
        sumacArr.append(nextNum)
        index += 1

print(len(sumacArr))
