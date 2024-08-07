h, m, want_h, want_m = map(int, input().split())
count = 0
while True:
    if h == want_h and m == want_m:
        break

    m += 1
    count += 1

    if m == 60:
        h += 1
        m = 0

print(count)