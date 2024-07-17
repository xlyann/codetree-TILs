n = int(input())
sum_val = 0
for i in range(1, n//2+1):
    if n % i == 0:
        sum_val += i

if n == sum_val:
    print('P')
else:
    print('N')