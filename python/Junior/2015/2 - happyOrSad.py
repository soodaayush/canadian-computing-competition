sentence = input()

happyCount = sentence.count(":-)")
sadCount = sentence.count(":-(")

if happyCount == 0 and sadCount == 0:
    print("none")
elif happyCount == sadCount:
    print("unsure")
elif happyCount > sadCount:
    print("happy")
else:
    print("sad")