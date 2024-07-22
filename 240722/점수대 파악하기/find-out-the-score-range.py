keep = [0]*10
num = list(map(int, input().split()))
for i in num:
    if i == 0:
        break
    elif i<10:
        continue
    else:
        keep[i//10-1] += 1
for j in range(10, 0, -1):
    print(j*10, '-', keep[j-1])