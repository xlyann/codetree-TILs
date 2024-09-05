n = int(input())
ground = list(int(input()) for _ in range(n))

ans = float('inf')
for i in range(84):
    money = 0
    for height in ground:
        if i > height:
            money += (i-height)**2
        if i+17 < height:
            money += (height-i-17)**2
    ans = min(ans, money)
print(ans)