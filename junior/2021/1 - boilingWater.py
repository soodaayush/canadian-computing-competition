b = int(input())

seaLevel = 0

kpa = 5 * b - 400

if kpa > 100:
    seaLevel = -1
elif kpa == 100:
    seaLevel = 0
else:
    seaLevel = 1

print(kpa)
print(seaLevel)

