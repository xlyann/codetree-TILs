n = int(input())
num_list = list(map(int, input().split()))

for i in range(1, n+1):
    new = []
    new.append(i)
    start = i
    ans = True
    for a in num_list:
        num = a-start
        new.append(num)
        start = num
    for j in range(1, n+1):
        if new.count(j) != 1:
            ans = False
            break
    if ans:
        print(*new)
        break