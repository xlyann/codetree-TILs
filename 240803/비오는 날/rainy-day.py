class rain:
    def __init__(self, y, d, weather):
        self.y = y
        self.d = d
        self.weather = weather
    
def vs(s_1, s_2):
    year1, month1, day1 = s_1.split('-')
    year2, month2, day2 = s_1.split('-')
    if year1 != year2:
        return year1 > year2
    if month1 != month2:
        return month1 > month2
    return day1 > day2
    
save = []
n = int(input())
for i in range(n):
    a, b, c = input().split()
    save.append(rain(a, b, c))

new = []
for i in save:
    if i.weather == 'Rain':
        new.append(i)

target = 0
for i, day in enumerate(new):
    if vs(new[target].y, day.y):
        target = i

print(new[target].y, new[target].d, new[target].weather)