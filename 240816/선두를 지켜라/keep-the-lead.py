times_a, times_b = map(int, input().split())
move_a = [0]
move_b = [0]

for i in range(times_a):
    v, t = map(int, input().split())
    for _ in range(t):
        move_a.append(move_a[-1] + v)

for i in range(times_b):
    v, t = map(int, input().split())
    for _ in range(t):
        move_b.append(move_b[-1] + v)

cnt = 0
old = 0

for i in range(1, len(move_a)):
    if move_a[i] == move_b[i]:
        continue
        
    new = move_a[i] - move_b[i]

    if old * new < 0:
        cnt += 1
    
    old = new

print(cnt)