n = int(input())
letter = list(input())

ans = 0
for i in range(1, n):
    for j in range(n-i+1):
        for k in range(j+1, n-i+1):
            if letter[j:j+i] == letter[k:k+i]:
                ans = i
print(ans+1)