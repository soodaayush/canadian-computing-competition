start = input().split(" ")
destination = input().split(" ")
steps = int(input())

distance = abs(int(start[0]) - int(destination[0])) + abs(int(start[1]) - int(destination[1]))

if distance <= steps and (steps - distance) % 2 == 0:
    print('Y')
else:
    print('N')