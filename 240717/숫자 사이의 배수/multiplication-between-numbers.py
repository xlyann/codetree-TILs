count = 0
sum_val = 0
a, b = map(int, input().split())
for i in range(a, b+1):
    if i%5 == 0:
        count += 1
        sum_val += i
    elif i%7 == 0:
        count += 1
        sum_val += i

print(sum_val, f'{sum_val/count:.1f}')