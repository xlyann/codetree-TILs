line = []
save = []
n = int(input())
for i in range(n):
    num, LorR = input().split()
    a = (int(num), LorR)
    save.append(a)

point = 0
for a, b in save:
    if b == 'R':
        if point + a > len(line):
            line = line + [0]*(point + a - len(line))
        
        for i in range(point, point + a):
            line[i] += 1
        
        point += a
    else:
        if point - a < 0:
            line = [0]*(abs(point-a)) + line
            point = 0
            for i in range(a):
                line[i] += 1
        
        else:
            for i in range(point-a, point):
                line[i] += 1
            
            point -= a
    
count = 0
for over_2 in line:
    if over_2 >= 2:
        count += 1
print(count)