count = 0
n = int(input())
while n<1000:
    count += 1
    if n%2 == 0:
        n *= 3
        n += 1
    else:
        n *= 2
        n += 2
print(count)