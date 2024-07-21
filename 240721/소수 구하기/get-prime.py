n = int(input())
for i in range(1, n+1):
    if i == 2 or i == 3:
        print(i, end = ' ')
        continue
    for j in range(2, i//2+1):
        if i%j == 0:
            break
        if j == i//2:
            print(i, end = ' ')