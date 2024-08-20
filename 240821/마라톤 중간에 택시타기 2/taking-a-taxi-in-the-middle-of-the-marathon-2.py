import sys

INT_MAX = sys.maxsize

n = int(input())
min_val = INT_MAX
checkpoint = [tuple(map(int, input().split())) for _ in range(n)]

def taxi_d(a, b, c, d):
    return abs(a-c) + abs(b-d)

for i in range(1, n-1):
    tmp = checkpoint[i]
    checkpoint.pop(i)
    sum_min = 0

    for j in range(n-2):
        a, b = checkpoint[j]
        c, d = checkpoint[j+1]
        sum_min += taxi_d(a, b, c, d)
    
    min_val = min(min_val, sum_min)

    checkpoint.insert(i, tmp)

print(min_val)