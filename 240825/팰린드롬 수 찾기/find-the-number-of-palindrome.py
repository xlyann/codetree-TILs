x, y = map(int, input().split())

ans = 0
for i in range(x, y+1):
    new = list(str(i))
    pellin = True
    for j in range(len(new)//2+1):
        if new[j] != new[len(new)-1-j]:
            pellin = False
            break
    if pellin:
        ans += 1
print(ans)