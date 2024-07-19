sat = False
a, b, c = map(int, input().split())
for i in range(a, b+1):
    if i%c == 0:
        sat = True

if sat:
    print('YES')
else:
    print('NO')