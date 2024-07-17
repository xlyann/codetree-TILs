a, b = map(int, input().split())

def sum_5(n, m):
    sum_val = 0
    for i in range(n, m+1):
        if i % 5 == 0:
            sum_val += i
    print(sum_val)

if a<b:
    sum_5(a, b)
else:
    sum_5(b, a)