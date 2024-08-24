a, b, c = map(int, input().split())

ans = 0
for i in range(1000):
    for j in range(1000):
        new = a*i + b*j
        if new > c:
            break
        ans = max(ans, new)
print(ans)