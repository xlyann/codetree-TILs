n = int(input())
line = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            arr = [0]*101
            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                a, b = line[l]
                for plus in range(a, b+1):
                    arr[plus] += 1
            guess = True
            for over_2 in arr:
                if over_2>=2:
                    guess = False
                    break
            if guess:
                ans += 1
print(ans)