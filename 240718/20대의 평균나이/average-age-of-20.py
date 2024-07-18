sum_val = 0
count = 0
while True:
    a = int(input())
    if 20<= a and a <= 29:
        sum_val += a
        count += 1
    else:
        print('{:.2f}'.format(sum_val/count))
        break