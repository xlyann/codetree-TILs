num = list(map(int, input().split()))
for i in range(1, 7):
    count = 0
    for j in num:
        if j == i:
            count += 1
    print(i, '-', count)