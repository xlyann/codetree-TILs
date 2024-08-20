a = list(map(int, list(input())))

def change(num):
    if num == 0:
        return 1
    return 0

max_val = 0

for i in range(len(a)):
    a[i] = change(a[i])
    sum_val = 0

    for j in a:
        sum_val = 2*sum_val + j
    
    max_val = max(max_val, sum_val)
    a[i] = change(a[i])
    
print(max_val)