a = list(map(int, input().split()))
for i in a:
    if i == 0:
        b = len(a)-a.index(i)
        print(sum(a[:-b]))
        break