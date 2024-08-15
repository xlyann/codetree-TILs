n = int(input())
_list = list(int(input()) for _ in range(n))
save = []

count = 1
for i in range(n):
    if i == 0:
        continue
    
    if _list[i] != _list[i-1]:
        save.append(count) 
        count = 1
    else:
        count += 1
    
    if i == n-1:
        save.append(count)

if n == 1:
    print(1)
else:
    print(max(save))