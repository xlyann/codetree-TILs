arr = [0]*101
n = int(input())
for _ in range(n):
    a, b = input().split()
    a = int(a)
    arr[a] = b

ans = 0
for i in range(101):
    for j in range(i, 101):
        if arr[i] != 0 and arr[j] != 0:
            cnt_G = arr[i:j+1].count('G')
            cnt_H = arr[i:j+1].count('H')
            if cnt_G == cnt_H or cnt_G == 0 or cnt_H == 0:
                val = j-i
                ans = max(ans, val)
print(ans)