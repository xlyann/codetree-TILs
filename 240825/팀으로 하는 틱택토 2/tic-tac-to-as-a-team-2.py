tictactoc = [list(map(int, list(input()))) for _ in range(3)]

def check(a, b):
    return (a==1 and b==2) or (a==2 and b==1)

ans = 0
for i in range(1, 10):
    for j in range(i+1, 10):
        for k in range(8):
            cnt_i = 0
            cnt_j = 0
            
            if k in [0, 1, 2]:
                cnt_i = tictactoc[k].count(i)
                cnt_j = tictactoc[k].count(j)
                if check(cnt_i, cnt_j):
                    ans += 1
                    break

            elif k in [3, 4, 5]:
                for l in range(3):
                    if tictactoc[l][k-3] == i:
                        cnt_i += 1
                    elif tictactoc[l][k-3] == j:
                        cnt_j += 1
                    else:
                        break
                if check(cnt_i, cnt_j):
                    ans += 1
                    break

            elif k == 6:
                for l in range(3):
                    if tictactoc[l][l] == i:
                        cnt_i += 1
                    elif tictactoc[l][l] == j:
                        cnt_j += 1
                    else:
                        break
                if check(cnt_i, cnt_j):
                    ans += 1
                    break

            else:
                for l in range(3):
                    if tictactoc[2-l][l] == i:
                        cnt_i += 1
                    elif tictactoc[2-l][l] == j:
                        cnt_j += 1
                    else:
                        break
                if check(cnt_i, cnt_j):
                    ans += 1
                    break
print(ans)