n, m = map(int, input().split())
num = list(map(int, input().split()))

for i in range(max(num), 5001):
    save = []
    limit = 0
    for j in num:
        if limit + j <= i:
            limit += j
            if j == num[-1]:
                save.append(limit)
        else:
            save.append(limit)
            limit = j
            if j == num[-1]:
                save.append(j)

    if len(save) == m:
        print(i)
        break