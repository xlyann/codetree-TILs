a = list(map(int, input().split()))
sum_val = 0
count = 0

for i in a:
    if i == 0:
        break
    if i%2 == 0:
        count += 1
        sum_val += i
print(count, sum_val)