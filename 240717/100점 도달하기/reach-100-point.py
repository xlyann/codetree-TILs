a = int(input())
for i in range(a, 101):
    if a >= 90:
        print('A', end = ' ')
    elif a>= 80:
        print('B', end = ' ')
    elif a>= 70:
        print('C', end = ' ')
    elif a>= 60:
        print('D', end = ' ')
    else:
        print('F', end = ' ')
    a += 1