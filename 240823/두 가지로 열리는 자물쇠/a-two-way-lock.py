n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def password(x, y, z):
    global a1, b1, c1, a2, b2, c2, n
    if (check(a1, x) and check(b1, y) and check(c1, z)) or (check(a2, x) and check(b2, y) and check(c2, z)):
        return 1
    return 0

def check(x, y):
    global n
    if abs(x-y)<=2 or x+n-y<=2 or y+n-x<=2:
        return 1
    return 0

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            ans += password(i, j, k)


print(ans)