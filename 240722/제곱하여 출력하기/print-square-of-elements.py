a = int(input())
num = list(map(int, input().split()))
sq = [i*i for i in num]
print(*sq)