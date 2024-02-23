dusaSize = int(input())

while True:
    yobiSize = int(input())

    if yobiSize < dusaSize:
        dusaSize += yobiSize

    if yobiSize >= dusaSize:
        break


print(dusaSize)