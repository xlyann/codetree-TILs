num = list(map(int, input().split()))
_min, _max = num[0], num[0]
for i in num:
    if i == 999 or i == -999:
        break
    elif i < _min:
        _min = i
    elif i > _max:
        _max = i

print(_max, _min)