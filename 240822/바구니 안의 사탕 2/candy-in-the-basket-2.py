n, k = map(int, input().split())
arr = [0]*1001
candy = list(tuple(map(int, input().split())) for _ in range(n))
for elem1, elem2 in candy:
    arr[elem2] += elem1

ans = 0
for i in range(k, 1001-k):
    sum_val = sum(arr[i-k:i+k+1])
    ans = max(ans, sum_val)
print(ans)