num = list(map(int, input().split()))
down500, up500 = 0, 1000
for i in num:
    if i > 500 and i < up500:
        up500 = i
    elif i < 500 and i > down500:
        down500 = i
print(down500, up500)