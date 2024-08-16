times_a, times_b = map(int, input().split())
move_a = [0]
move_b = [0]

for i in range(times_a):
    d, t = input().split()
    d = int(d)
    for _ in range(d):
        move_a.append(move_a[-1] + (1 if t == 'R' else -1))

for i in range(times_b):
    d, t = input().split()
    d = int(d)
    for _ in range(d):
        move_b.append(move_b[-1] + (1 if t == 'R' else -1))

if len(move_a) > len(move_b):
    move_b += [move_b[-1]]*(len(move_a)-len(move_b))
else:
    move_a += [move_a[-1]]*(len(move_b)-len(move_a))

cnt = 0

for i in range(1, len(move_a)):
    if move_a[i] == move_b[i] and move_a[i-1] != move_b[i-1]:
        cnt += 1

print(cnt)