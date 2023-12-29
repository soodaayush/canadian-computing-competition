small = int(input())
medium = int(input())
large = int(input())

happinessScore = 1 * small + 2 * medium + 3 * large

if happinessScore >= 10:
    print("happy")
else:
    print("sad")