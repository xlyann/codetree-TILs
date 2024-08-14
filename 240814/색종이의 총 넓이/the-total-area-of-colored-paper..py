n = int(input())
offset = 100
coordi = list([0]*201 for _ in range(201))

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+8):
        for j in range(b, b+8):
            coordi[i][j] = 1

count = 0
for find_1 in coordi:
    count += find_1.count(1)

print(count)