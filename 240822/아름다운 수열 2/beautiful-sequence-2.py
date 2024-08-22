a, b = map(int, input().split())
num_a = list(map(int, input().split()))
num_b = list(map(int, input().split()))
num_b.sort()

ans = 0
for i in range(a-b+1):
    new = []
    for j in range(i, i+b):
        new.append(num_a[j])
    new.sort()
    if new == num_b:
        ans += 1
print(ans)