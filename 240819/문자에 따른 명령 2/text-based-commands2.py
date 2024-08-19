dir_num = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

command = input()
command = list(command)
for i in command:
    if i == 'R':
        dir_num = (dir_num+1)%4
    if i == 'L':
        dir_num = (dir_num+3)%4
    if i == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)