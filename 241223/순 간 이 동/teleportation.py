a, b, tp_1, tp_2 = map(int, input().split())
ans = abs(b-a)

new1 = abs(a-tp_1) + abs(b-tp_2)
new2 = abs(b-tp_1) + abs(a-tp_2)

print(min(ans, new1, new2))