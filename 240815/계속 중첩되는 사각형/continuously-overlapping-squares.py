n = int(input())
coordi = list([0]*200 for _ in range(200))
offset = 100

def paint(a, b, c, d, num):
    global offset
    for i in range(a + offset, c + offset):
        for j in range(b + offset, d + offset):
            coordi[i][j] = num

for i in range(n):
    _list = list(map(int, input().split()))
    paint(*_list, i%2)

count = 0

for find_1 in coordi:
    count += find_1.count(1)

print(count)