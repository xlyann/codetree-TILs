n = int(input())
guess = [list(map(int, input().split())) for _ in range(n)]

def in_num_1(num, a, b, c):
    x, y, z = num//100, num%100//10, num%10
    cnt = 0
    if x == a:
        cnt += 1
    if y == b:
        cnt += 1
    if z == c:
        cnt += 1
    return cnt

def in_num_2(num, a, b, c):
    x, y, z = num//100, num%100//10, num%10
    cnt = 0
    if x == b or x == c:
        cnt += 1
    if y == a or y == c:
        cnt += 1
    if z == a or z == b:
        cnt += 1
    return cnt

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i==j or j==k or k==i:
                continue

            ok = 0
            for num, cnt_1, cnt_2 in guess:
                check_1 = 0
                check_2 = 0
                if in_num_1(num, i, j, k) == cnt_1 and in_num_2(num, i, j, k) == cnt_2:
                    ok += 1              

            if ok == n:
                ans += 1
print(ans)