n = int(input())
for i in range(n):
    count = 0
    a = int(input())
    while True:
        if a == 1:
            break
        if a%2 == 0:
            a //= 2
        else:
            a *= 3
            a += 1
        count += 1
    print(count)