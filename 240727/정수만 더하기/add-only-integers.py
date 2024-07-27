a = input()
sum_val = 0
for i in a:
    if i.isdigit():
        sum_val += int(i)
print(sum_val)