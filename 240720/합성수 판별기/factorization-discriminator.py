sat = False
n = int(input())
for i in range(2, n):
    if n%i == 0:
        sat = True
        break

if sat:
    print('C')
else:
    print('N')