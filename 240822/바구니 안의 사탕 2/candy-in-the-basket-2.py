n, k = map(int, input().split())
arr = [0]*101
candy = list(tuple(map(int, input().split())) for _ in range(n))
for elem1, elem2 in candy:
    arr[elem2] += elem1

current_sum = sum(arr[:2*k+2])
max_sum = current_sum

for i in range(1, 101 - 2*k):
    current_sum = current_sum - arr[i-1] + arr[i + 2*k ]
    max_sum = max(max_sum, current_sum)
print(max_sum)