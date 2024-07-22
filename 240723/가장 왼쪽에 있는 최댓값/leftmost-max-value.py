a = int(input())
num = list(map(int, input().split()))
cut = a-1
while True:
    new = num[:cut]
    if new == []:
        break
    _max = max(new)
    find = num.index(_max)
    
    print(find+1, end = ' ')
    cut = find-a