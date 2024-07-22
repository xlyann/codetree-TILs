a = int(input())
num = list(map(int, input().split()))
bet = 100
for i in range(a-1):
    if num[i+1] - num[i] < bet:
        bet = num[i+1] - num[i]
print(bet)