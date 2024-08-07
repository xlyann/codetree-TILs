num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d, want_m, want_d = map(int, input().split())
count = 0

while True:
    if m == want_m and d == want_d:
        break
    
    d += 1
    count += 1

    if d > num_of_days[m]:
        m += 1
        d = 1

print(count+1)