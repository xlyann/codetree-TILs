max_cnt = 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n-2):
        for k in range(i, n):
            for l in range(j+3, n-2):
                max_cnt = max(max_cnt, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[k][l] + arr[k][l+1] + arr[k][l+2])

print(max_cnt)