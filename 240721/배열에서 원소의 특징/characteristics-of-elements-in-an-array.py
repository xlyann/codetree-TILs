a = list(map(int, input().split()))
for i in a:
    if i%3 == 0:
        b = a.index(i)
        print(a[b-1])
        break