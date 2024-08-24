n, b = map(int, input().split())
gift = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    gift_sale = []
    money = b
    cnt = 0
    for j in range(n):
        if i == j:
            gift_sale.append(gift[j][0]//2+gift[j][1])
        else:
            gift_sale.append(gift[j][0]+gift[j][1])
    gift_sale.sort()
    
    for k in range(n):
        money -= gift_sale[k]
        if money < 0:
            break
        cnt += 1
    
    ans = max(ans, cnt)
print(ans)