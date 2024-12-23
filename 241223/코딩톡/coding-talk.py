n, m, p = map(int, input().split())
people = []
for i in range(n):
    people.append(chr(65+i))

save = list(list(input().split()) for _ in range(m))

for i in range(m):
    if i < p-1:
        continue
    if i == p-1 and save[i][1] == '0':
        people.clear()
        break
    if i == p-1 and i != 0:
        for j in range(1, 100):
            if save[i][1] == save[i-j][1] and i-j >= 0:
                if save[i-j][0] in people:
                    people.remove(save[i-j][0])
                else:
                    continue
            else:
                break
            
    if save[i][0] in people:
        people.remove(save[i][0])

print(*people)