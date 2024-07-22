a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Q = 'No'

for i in range(a):
    if A[i] == B[0]:
        if A[i:i+b] == B:
            Q = 'Yes'
            break

print(Q)