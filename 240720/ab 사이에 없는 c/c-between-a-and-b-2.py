sat = True
a, b, c = map(int, input().split())
for i in range(a, b+1):
    if i%c != 0:
        sat = False
        break

if sat == False:
    print('YES')
else:
    print('NO')