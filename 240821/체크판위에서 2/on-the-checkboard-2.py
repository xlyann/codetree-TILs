r, c = map(int, input().split())
chess = [list(input().split()) for _ in range(r)]

sum_val = 0

for i in range(1, r-1):
    for j in range(1, c-1):
        if chess[0][0] != chess[i][j]:
            for i2 in range(i+1, r-1):
                for j2 in range(j+1, c-1):
                    if chess[i2][j2] != chess[i][j]:
                        sum_val += 1
                    

if chess[0][0] == chess[r-1][c-1]:
    sum_val = 0

print(sum_val)