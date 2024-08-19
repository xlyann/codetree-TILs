x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
mapper = {'E':0, 'S':1, 'W':2, 'N':3}

n = int(input())
_list = [tuple(input().split()) for _ in range(n)]

answer = -1
cnt = 0

for elem1, elem2 in _list:
    distance = int(elem2)
    rotate = mapper[elem1]

    for i in range(distance):
        x, y = x+dx[rotate], y+dy[rotate]
        cnt += 1
        if x==0 and y==0:
            answer = cnt
            break
    
    if x==0 and y==0:
        break

print(answer)