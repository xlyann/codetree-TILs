num = input()
digit = list(map(int, list(num)))
sum_val = 0

for i in digit:
    sum_val = sum_val*2 + i

print(sum_val)