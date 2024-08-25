n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]

def line(a):
    for i, (x, y) in enumerate(point):
        if a <= 10 and a == x:
            check[i] = 1
        if a >= 11 and a-11 == y:
            check[i] = 1


ans = 0
for i in range(22):
    for j in range(i+1, 22):
        for k in range(j+1, 22):
            check = [0]*n
            line(i)
            line(j)
            line(k)
            if check.count(1) == n:
                ans = 1
print(ans)