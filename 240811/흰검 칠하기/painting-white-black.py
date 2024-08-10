line = ['']
save = []
change = []
n = int(input())
for i in range(n):
    num, LorR = input().split()
    a = (int(num), LorR)
    save.append(a)

point = 0
for a, b in save:
    if b == 'R':
        if point + a > len(line):
            line = line + ['']*(point + a - len(line))
        
        for i in range(point, point + a):
            line[i] += 'B'
        
        point += a - 1
    else:
        if point - a <= -1:
            line = ['']*(abs(point-a+1)) + line
            point = 0
            for i in range(a):
                line[i] += 'W'
        
        else:
            for i in range(point, point-a, -1):
                line[i] += 'W'
            
            point -= a - 1

W, B, G = 0, 0, 0
for color in line:
    if color.count('W') >= 2 and color.count('B') >= 2:
        G += 1
    elif color[-1] == 'W':
        W += 1
    else:
        B += 1

print(W, B, G)