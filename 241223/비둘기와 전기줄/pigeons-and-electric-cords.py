elec_line = [2]*11
times = int(input())

ans = 0
for i in range(times):
    bird, position = map(int, input().split())
    if elec_line[bird] == 2:
        elec_line[bird] = position
    if elec_line[bird] != position:
        ans += 1
        elec_line[bird] = position

print(ans)