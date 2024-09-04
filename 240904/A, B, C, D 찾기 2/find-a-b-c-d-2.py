num_list = list(map(int, input().split()))
num_list.sort()

def possible(a, b, c, d):
    new = [a,b,c,d]
    save = []
    for i in range(4):
        for j in range(i+1, 4):
            save.append(new[i]+new[j])
    limit = a+b+c+d
    save.append(limit)
    for i in range(4):
        save.append(new[i])
        save.append(limit-new[i])
    save.sort()
    if save == num_list:
        return True
    return False

for i in range(1, 37):
    for j in range(i, 37):
        for k in range(j, 37):
            for l in range(k, 37):
                if i+j+k+l >40:
                    continue
                if possible(i,j,k,l):
                    print(i,j,k,l)
                    break