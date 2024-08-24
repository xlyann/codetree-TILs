times, n = map(int, input().split())
record = [list(map(int, input().split())) for _ in range(times)]

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        guess = True
        for k in range(times):
            if record[k].index(i+1) > record[k].index(j+1):
                guess = False
                break
        if guess:
            ans += 1

print(ans)