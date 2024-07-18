sum_val = 0
n = int(input())
for i in range(1, 101):
    sum_val += i
    if sum_val >= n:
        num = i
        break
print(num)