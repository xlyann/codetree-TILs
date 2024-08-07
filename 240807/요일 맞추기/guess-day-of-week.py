save = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day, w_month, w_day = map(int, input().split())
count = 1

def date(n, m):
    sum_val = 0
    for i in range(1, n):
        sum_val += num_of_days[i]
    
    sum_val += m
    return sum_val

if date(month, day) > date(w_month, w_day):
    value = -1
else:
    value = 1

while True:
    if month == w_month and day == w_day:
        break
    
    day += value
    count += value

    if day == 0:
        month += -1
        day = num_of_days[month]
    
    if day > num_of_days[month]:
        month += 1
        day = 1

    if count == -1:
        count = 6
    
    if count == 7:
        count = 0

print(save[count])