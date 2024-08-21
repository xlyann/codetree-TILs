import sys

INT_MAX = sys.maxsize

n = int(input())
need = list(int(input()) for _ in range(n))

min_sum = INT_MAX
for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += (j-i)%n*need[j]
    
    min_sum = min(min_sum, sum_val)

print(min_sum)