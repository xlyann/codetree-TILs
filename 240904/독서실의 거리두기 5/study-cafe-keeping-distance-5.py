n = int(input())
seat = list(map(int, list(input())))

ans = 0
for i in range(n):
    if seat[i] == 1:
        continue
    seat[i] = 1
    start = seat.index(1)
    diff_min = 90

    for j in range(start+1, n):
        if seat[j] == 1:
            diff = j-start
            diff_min = min(diff_min, diff)
            start = j
    
    ans = max(ans, diff_min)
    seat[i] = 0

print(ans)