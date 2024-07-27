n = int(input())
sum_val = 0
for i in range(n):
    sum_val += int(input())

new = str(sum_val)
print(new[1:] + new[0])