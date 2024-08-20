n = int(input())
people = list(map(int, input().split()))
min_sum = []

for i in range(n):
    sum_diff = 0

    for j in range(n):
        sum_diff += abs(i-j)*people[j]
    
    min_sum.append(sum_diff)

print(min(min_sum))