import sys

INT_MAX = sys.maxsize

n = int(input())
point = list(tuple(map(int, input().split())) for _ in range(n))

def distance_sq(a, b, c, d):
    return (a-c)**2 + (b-d)**2

ans = INT_MAX
for i in range(n):
    for j in range(i+1, n):
        a, b = point[i]
        c, d = point[j]
        ans = min(ans, distance_sq(a, b, c, d))
        
print(ans)