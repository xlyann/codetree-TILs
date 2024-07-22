keep = [0]*9
num = list(map(int, input().split()))
for i in num:
    if i == 0:
        break
    elif i//10 == 0:
        continue
    else:
        keep[i//10-1] += 1
for j in range(1, 10):
    print(j, '-', keep[j-1])