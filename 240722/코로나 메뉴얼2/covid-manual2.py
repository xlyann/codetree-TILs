corona = [0]*4
for i in range(3):
    symp, temp = input().split()
    if symp == 'Y':
        if int(temp)>=37:
            corona[0] += 1
        else:
            corona[2] += 1
    else:
        if int(temp)>=37:
            corona[1] += 1
        else:
            corona[3] += 1
if corona[0] >= 2:
    corona.append('E')
print(*corona)