a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikkySteps = 0
byronSteps = 0

forward = True

for i in range(10000000):
    if forward and (nikkySteps + a <= s):
        nikkySteps += a
        s -= a
        forward = False
    else:
        nikkySteps -= b
        nikkySteps -= b

print(nikkySteps)