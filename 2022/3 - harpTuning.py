letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "-0123456789"
string = ""

instructions = input()
instructions = list(instructions)

for i in range(len(instructions)):
    if instructions[i] in letters:
        print(instructions[i])

        if instructions[i - 1] in numbers:
            instructions.insert(i, "*")

instructions.pop(0)

print(instructions)

for i in instructions:
    string += i

string = string.replace("+", " tighten ")
string = string.replace("-", " loosen ")
string = string.replace("*", "\n")

print(string)
