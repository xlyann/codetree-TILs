cnt = 0
n = int(input())
height = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if height[i] <= height[j] and height[j] <= height[k]:
                cnt += 1

print(cnt)