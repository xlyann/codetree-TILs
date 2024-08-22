n, k = map(int, input().split())
num = list(tuple(input().split()) for _ in range(n))

num.sort(key = lambda x:-int(x[0]))
arr = [0]*(int(num[0][0])+1)

for elem1, elem2 in num:
    if elem2 == 'G':
        arr[int(elem1)] = 1
    else:
        arr[int(elem1)] = 2

ans = 0
for i in range(len(arr)-k):
    sum_val = 0
    for j in range(i, i+k+1):
        sum_val += arr[j]
    ans = max(ans, sum_val)
print(ans)