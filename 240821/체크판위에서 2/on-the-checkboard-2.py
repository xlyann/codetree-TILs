r, c = map(int, input().split())
chess = [list(input().split()) for _ in range(r)]

sum_val = 0

for i in range(1, r-2):
    for j in range(1, c-2):
        if chess[0][0] != chess[i][j]:
            sum_val += (i-2)*(j-2) + (r-2-i) * (c-2-j)

if chess[0][0] == chess[r-1][c-1]:
    sum_val = 0

print(sum_val)