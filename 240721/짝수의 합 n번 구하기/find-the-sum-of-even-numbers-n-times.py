n = int(input())
for i in range(n):
    sum_val = 0
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if j%2 == 0:
            sum_val += j
    print(sum_val)