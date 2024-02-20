values = {"A": 0, "B": 0}
currentInput = input().split(" ")

while currentInput[0] != "7":
    if currentInput[0] == "1":
        values[currentInput[1]] = int(currentInput[2])
    elif currentInput[0] == "2":
        print(values[currentInput[1]])
    elif currentInput[0] == "3":
        values[currentInput[1]] = values[currentInput[1]] + values[currentInput[2]]
    elif currentInput[0] == "4":
        values[currentInput[1]] = values[currentInput[1]] * values[currentInput[2]]
    elif currentInput[0] == "5":
        values[currentInput[1]] = values[currentInput[1]] - values[currentInput[2]]
    elif currentInput[0] == "6":
        values[currentInput[1]] = values[currentInput[1]] // values[currentInput[2]]
    currentInput = input().split()
