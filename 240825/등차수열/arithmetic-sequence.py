n = int(input())
num = list(map(int, input().split()))
save = []

for i in range(n):
    for j in range(i+1, n):
        save.append((num[i]+num[j])/2)

ans = 0
for k in range(100):
    ans = max(ans, save.count(k))
print(ans)