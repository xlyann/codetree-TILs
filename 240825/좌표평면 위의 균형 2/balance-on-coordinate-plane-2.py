n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]

def quarter(x, y, a, b):
    if x<a and y<b:
        new[0] += 1
    elif x>a and y<b:
        new[1] += 1
    elif x>a and y>b:
        new[2] += 1
    else:
        new[3] += 1

ans = 9999999
for i in range(2, 101, 2):
    for j in range(2, 101, 2):
        new = [0]*4
        for x, y in point:
            quarter(x, y, i, j)
        ans = min(ans, max(new))
print(ans)