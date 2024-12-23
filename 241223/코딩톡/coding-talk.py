n, m, p = map(int, input().split())
people = []
for i in range(n):
    people.append(chr(65+i))

for i in range(m):
    who, read = input().split()
    if i < p-1:
        continue
    if who in people:
        people.remove(who)

print(*people)