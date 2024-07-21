n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        if i > j:
            print(' ', end = ' ')
        else:
            count += 1
            print(count, end = ' ')
        if count == 9:
            count = 0
    print()