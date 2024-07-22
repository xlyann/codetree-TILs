a = int(input())
num = list(map(int, input().split()))

if num.count(max(num)) == 2:
    print(max(num), max(num))
else:
    if num[0] > num[1]:
        _1, _2 = num[0], num[1]
    else:
        _1, _2 = num[1], num[0]
    
    for i in num[2:]:
        if i>_1:
            _1, _2 = i, _1
        elif i>_2:
            _2 = i
    
    print(_1, _2)