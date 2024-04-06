n = int(input())
k = int(input())

shiftySum = []
power = 1

for i in range(k):
    shiftySum.append(int(str(n) + "0" * power))
    power = power + 1

print(sum(shiftySum) + n)
