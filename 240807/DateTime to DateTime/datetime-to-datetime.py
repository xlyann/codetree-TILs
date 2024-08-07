w_day, w_hour, w_minute = map(int, input().split())
count = 0
day, hour, minute = 11, 11, 11

if w_day < 11:
    count = -1
elif w_hour < 11:
    count = -1
elif w_minute < 11:
    count = -1
else:
    while True:
        if day == w_day and hour == w_hour and minute == w_minute:
            break

        minute += 1
        count += 1

        if minute == 60:
            hour += 1
            minute = 0

        if hour == 24:
            day += 1
            hour = 0

print(count)