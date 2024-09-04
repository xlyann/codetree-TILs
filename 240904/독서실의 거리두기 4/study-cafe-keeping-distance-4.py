n = int(input())
seat = list(map(int, list(input())))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 or seat[j] == 1:
            continue
        seat[i], seat[j] = 1, 1
        start = seat.index(1)

        diff_min = 100
        for k in range(start+1, n):
            if seat[k] == 1:
               diff = k-start
               diff_min = min(diff_min, diff)
               start = k
               
        ans = max(ans, diff_min)
        seat[i], seat[j] = 0, 0
        
print(ans)