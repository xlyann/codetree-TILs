start = 0
times_a, times_b = map(int, input().split())
move_a = [0]
move_b = [0]

def move(num, ab):
    for i in range(num):
        LR, distance = input().split()
        distance = int(distance)

        if LR == 'L':
            stand = -1
        else:
            stand = 1

        if ab == 'a':
            for _ in range(distance):
                move_a.append(move_a[-1] + stand)
        else:
            for _ in range(distance):
                move_b.append(move_b[-1] + stand)

move(times_a, 'a')
move(times_b, 'b')

limit = min(len(move_a), len(move_b))

meet = -1
for i in range(1, limit):
    if move_a[i] == move_b[i]:
        meet = i
        break

print(meet)