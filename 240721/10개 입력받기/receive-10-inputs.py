a = list(map(int, input().split()))
for i in a:
    if i == 0:
        a = a[:-(10-a.index(0))]
print(f'{sum(a)} {sum(a)/len(a):.1f}')