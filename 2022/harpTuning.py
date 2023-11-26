def harpTuning(instructions):
    instruction = ""
    cleanInstructions = []

    for i in instructions:
        if i == "+":
            instruction += " tighten "

        if i == "-":
            instruction += " loosen "

        if i.isnumeric():
            instruction += i
            cleanInstructions.append(instruction)
            instruction = ""
        elif i != "+" and i != "-":
            instruction += i

    return cleanInstructions


print(harpTuning("AFB+8SC-4H-2GDPE+9"))