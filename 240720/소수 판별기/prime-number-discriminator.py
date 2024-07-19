sat = True
n = int(input())
for i in range(2, n):
    if n%i == 0:
        sat = False
        break

if sat:
    print('P')
else:
    print('C')