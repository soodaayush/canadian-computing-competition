from datetime import datetime
# 05:00

# 7 - 10 AM RUSH HOUR
# 3 - 07 PM RUSH HOUR 15 - 19

# NORMAL TIME    - 2 HOURS
# RUSH HOUR TIME - 4 HOURS


startTime = "05:00" # str(input())
s_time = startTime.split(":")
hr = s_time[0]
min = s_time[1]
normal_hours = 2

if ((int(hr) + normal_hours >= 7) and int(min) > 0) or int(hr) + int(min) + normal_hours <= 10:
    print('in rush hour')
else:
    print('not rush hour')


print(hr)
print(min)
