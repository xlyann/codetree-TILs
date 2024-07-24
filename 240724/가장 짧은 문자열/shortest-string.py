_min = 21
_max = 0
for i in range(3):
    a = input()
    if len(a) < _min:
        _min = len(a)
    
    if len(a) > _max:
        _max = len(a)

print(_max-_min)