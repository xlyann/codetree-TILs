save = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day, w_month, w_day = map(int, input().split())
d_week = input()
need = save.index(d_week)
rotate = 1
count = 0

if rotate == need:
    count += 1

while True:
    if month == w_month and day == w_day:
        break
    
    day += 1
    rotate += 1
    
    if day > num_of_days[month]:
        month += 1
        day = 1

    if rotate > 6:
        rotate = 0

    if rotate == need:
        count += 1

print(count)