a = int(input())
num = list(map(int, input().split()))
for i in range(1, 10):
    count = 0
    for j in num:
        if j == i:
            count += 1
    print(count)