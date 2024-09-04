n = int(input())
seat = list(map(int, list(input())))

ans = 0
for i in range(n):
    if seat[i] == 1:
        continue
    left, right = 0, 0

    for j in range(i, -1, -1):
        if seat[j] == 1:
            break
        left += 1

    for k in range(i, n):
        if seat[k] == 1:
            break
        right += 1
    
    if i == 0:
        ans = max(ans, right)
    elif i == n-1:
        ans = max(ans, left)
    else:
        ans = max(ans, min(left, right))
print(ans)