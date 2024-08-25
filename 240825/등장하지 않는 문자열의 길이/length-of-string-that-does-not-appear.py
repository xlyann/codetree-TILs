n = int(input())
letter = list(input())

ans = 0
for i in range(1, n//2+1):
    for j in range(n-i+1):
        for k in range(j+i, n-i+1):
            if letter[j:j+i] == letter[k:k+i]:
                ans = i
print(ans+1)