n = int(input())
count = 0
for i in range(n):
    a = list(map(int, input().split()))
    avg = sum(a)/len(a)
    if avg >= 60:
        print('pass')
        count += 1
    else:
        print('fail')
print(count)