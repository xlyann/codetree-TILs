arr = [list(map(int, input().split())) for _ in range(19)]
winner = 0

def win(a, b):
    if b <= 14 and win_row(a, b):
        return 1
    if a >= 14 and win_col(a, b):
        return 1
    if a <= 14 and b >= 14 and win_dia_L(a, b):
        return 1
    if a>=4 and b>=4 and win_dia_R(a, b):
        return 1
    return 0

def win_row(a, b):
    _list = []
    for i in range(0, 5):
        _list.append(arr[a][b+i])
    new = set(_list)
    if len(new) == 1:
        return 1
    return 0

def win_col(a, b):
    _list = []
    for i in range(0, 5):
        _list.append(arr[a+i][b])
    new = set(_list)
    if len(new) == 1:
        return 1
    return 0

def win_dia_L(a, b):
    _list = []
    for i in range(0, 5):
        _list.append(arr[a+i][b+i])
    new = set(_list)
    if len(new) == 1:
        return 1
    return 0

def win_dia_R(a, b):
    _list = []
    for i in range(0, 5):
        _list.append(arr[a-i][b+i])
    new = set(_list)
    if len(new) == 1:
        return 1
    return 0


for i in range(19):
    for j in range(19):
        if arr[i][j] != 0 and win(i, j):
            winner = arr[i][j]
            if win_row(i, j):
                x, y = i, j+2
            elif win_col(i, j):
                x, y = i+2, j
            elif win_dia_L(i, j):
                x, y = i+2, j+2
            elif win_dia_R(i, j):
                x, y = i-2, j+2
            break

print(winner)
if winner != 0:
    print(x+1, y+1)