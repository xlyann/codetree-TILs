n = int(input())
sum_val = 0

for i in range(n):
    sum_val += int(input())

print(sum_val, '{:.1f}'.format(sum_val/n))