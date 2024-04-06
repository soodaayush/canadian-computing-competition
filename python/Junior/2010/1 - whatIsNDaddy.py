selectedNum = int(input())

if selectedNum % 5 == 2 or selectedNum % 5 == 3:
    print(2)
else:
    if selectedNum <= 5:
        if selectedNum == 1:
            print(1)
        elif selectedNum >= 4:
            print(3)
    elif selectedNum > 5:
        if selectedNum % 5 == 1:
            print(3)
        elif selectedNum % 5 >= 4 or selectedNum % 5 == 0:
            print(1)
