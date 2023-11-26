def specialEvent(people, list):
    days = []
    result = []

    for i in list:
        days.append(i.count("Y"))

    day = max(days)

    for index, item in enumerate(days):
        if item == day:
            result.append(index + 1)

    return result


print(specialEvent(3, [["Y", ".", ".", ".", "Y"], ["Y", "Y", "Y", "Y", "."], [".", "Y", ".", "Y", "."],
                       [".", ".", "Y", ".", "."], ["Y", "Y", ".", "Y", "Y"]]))