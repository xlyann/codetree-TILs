count = 0
n = int(input())
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            count += 1
            print(count, end=" ")
    else:
        for j in range(n):
            print(count, end=" ")
            count -= 1
    count += n
    print()