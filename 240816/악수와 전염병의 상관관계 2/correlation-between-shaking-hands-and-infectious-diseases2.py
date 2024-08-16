people, limit, first, times = map(int, input().split())
cnt = [0] * (people + 1)
order = []
hand = []
infect = [0] * (people + 1)

infect[first] = 1
cnt[first] = limit

for _ in range(times):
    s, x, y = map(int, input().split())
    order.append(s)
    order.sort()
    where = order.index(s)
    hand.insert(where, (x,y))

for person1, person2 in hand:
    if infect[person1] == 0 and infect[person2] == 0:
        continue
    
    if infect[person1] == 1:
        if cnt[person1] == 0:
            continue
    
        if infect[person2] == 0:
            cnt[person2] = limit
            infect[person2] = 1
    
        cnt[person1] -= 1
    
    else:
        if cnt[person2] == 0:
            continue
        
        if infect[person1] == 0:
            cnt[person1] = limit
            infect[person1] = 1
        
        cnt[person2] -= 1

for virus in infect[1:]:
    print(virus, end = '')