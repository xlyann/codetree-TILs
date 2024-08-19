x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3
answer = -1
cnt = 0
_list = list(input())

for i in _list:
    cnt += 1
    if i == 'R':
        dir_num = (dir_num+1)%4
    if i == 'L':
        dir_num = (dir_num+3)%4
    if i == 'F':
        x, y = x+dx[dir_num], y+dy[dir_num]
        if x == 0 and y == 0:
            answer = cnt
            break

print(answer)