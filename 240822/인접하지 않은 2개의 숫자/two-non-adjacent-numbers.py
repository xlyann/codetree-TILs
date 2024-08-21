n = int(input())
num_list = list(map(int, input().split()))
max_sum = 0

for i in range(n):
    for j in range(i+2, n):
        sum_val = num_list[i] + num_list[j]
        max_sum = max(max_sum, sum_val)

print(max_sum)