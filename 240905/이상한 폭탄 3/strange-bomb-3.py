n, k = map(int, input().split())
num = list(int(input()) for _ in range(n))

def in_range(a):
    global n
    return 0<=a and a<=n-1

boom = {}
for i in range(n):
    bomb = num[i]
    for j in range(i-k, i+k+1):
        if in_range(j) and i!=j and num[j] == bomb:
            if bomb in boom:
                boom[bomb] += 1
            else:
                boom[bomb] = 1
            break

new_boom = sorted(boom.items(), key = lambda x:(-x[1], -x[0]))

if boom == {}:
    print(0)
else:
    print(new_boom[0][0])