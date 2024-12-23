a, b, c = map(int, input().split())
diff = [abs(a-b), abs(c-b), abs(a-c)]
if diff.count(1) == 2:
    print(0)
elif diff.count(2) >= 1:
    print(1)
else:
    print(2)