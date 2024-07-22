a = int(input())
num = list(map(int, input().split()))
cut = 0
new = num[:]
while new != []:
    _max = max(new)
    find = num.index(_max)
    
    print(find+1, end = ' ')
    cut = find-a
    new = num[:cut]