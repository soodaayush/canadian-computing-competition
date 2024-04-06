a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())


def stepCalculator(stepsForward, stepsBackward, maxSteps):
    total = 0
    steps = 0

    while total < maxSteps:
        if total + stepsForward <= maxSteps:
            steps += stepsForward
            total += stepsForward
        elif total + stepsForward > maxSteps:
            steps += maxSteps - total
            total += maxSteps - total
        if total + stepsBackward <= maxSteps:
            steps -= stepsBackward
            total += stepsBackward
        elif total + stepsBackward > maxSteps:
            steps -= maxSteps - total
            total += maxSteps - total
    return steps


if stepCalculator(a, b, s) > stepCalculator(c, d, s):
    print("Nikky")
elif stepCalculator(c, d, s) > stepCalculator(a, b, s):
    print("Byron")
else:
    print("Tied")
