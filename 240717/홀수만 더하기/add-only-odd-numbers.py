sum_val = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a % 2 == 1 and a % 3 == 0:
        sum_val += a
print(sum_val)