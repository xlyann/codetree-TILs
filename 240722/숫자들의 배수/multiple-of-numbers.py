a = int(input())
if a%5 == 0:
    num = [i*a for i in range(1, 3)]
    print(*num)
else:
    num = [i*a for i in range(1, 11)]
    print(*num)