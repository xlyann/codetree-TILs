n = int(input())
start = list(map(int,input().split()))
final = list(map(int,input().split()))
ans = 0

for i in range(n-1):
    diff = start[i] - final[i]
    ans += diff
    start[i+1] += diff

print(ans)