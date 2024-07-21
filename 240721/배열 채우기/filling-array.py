a = list(map(int, input().split()))
b = []
for i in a:
    if i == 0:
        break
    b.insert(0, i)
print(*b)