count = 0
a, b = map(int, input().split())
for i in range(a, b+1):
    sum_val = 0
    for j in range(1, i//2+1):
        if i%j == 0:
            sum_val += 1
    if sum_val == 2:
        count += 1
print(count)