x, y = map(int, input().split())
ans = 0
for i in range(x, y+1):
    save = list(str(i))
    new = set(save)
    if len(new) == 2 and (save.count(min(new)) == 1 or save.count(max(new)) == 1):
        ans += 1
print(ans)