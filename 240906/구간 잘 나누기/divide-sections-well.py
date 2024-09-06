n, m = map(int, input().split())
num = list(map(int, input().split()))

for i in range(100, 101):
    save = []
    limit = 0
    for j in range(n):
        if limit + num[j] <= i:
            limit += num[j]
            if j == n-1:
                save.append(limit)
        else:
            save.append(limit)
            limit = num[j]
            if j == n-1:
                save.append(num[j])

    if len(save) <= m:
        print(i)
        break