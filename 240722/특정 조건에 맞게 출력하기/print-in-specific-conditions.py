num = list(map(int, input().split()))
for i in num:
    if i == 0:
        break
    elif i%2 == 1:
        print(i+3, end = ' ')
    else:
        print(i//2, end = ' ')