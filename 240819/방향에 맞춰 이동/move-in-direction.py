rotate = ['E', 'S', 'W', 'N']
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())
x, y = 0, 0
for i in range(n):
    a, b = input().split()
    b = int(b)

    new = rotate.index(a)
    x, y = x + b*dx[new], y + b*dy[new]

print(x, y)