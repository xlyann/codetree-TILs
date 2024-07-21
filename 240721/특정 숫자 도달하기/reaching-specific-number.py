a = list(map(int, input().split()))

for i in a:
    if i >= 250:
        b = a.index(i)
        break
a = a[:-b]
print(sum(a), '{:.1f}'.format(sum(a)/len(a)))