n, k = map(int, input().split())
num = list(map(int, input().split()))

ans = float('inf')
for i in range(1, 10001):
    cnt = 0
    for number in num:
        if i > number:
            cnt += i-number
        if i+k < number:
            cnt += number-i-k
    ans = min(ans, cnt)
print(ans)