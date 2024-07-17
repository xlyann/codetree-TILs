count = 0
sum_val = 0
for i in range(10):
    a = int(input())
    if 0<= a and a<= 200:
        count += 1
        sum_val += a

print(sum_val, '{:.1f}'.format(sum_val/count))