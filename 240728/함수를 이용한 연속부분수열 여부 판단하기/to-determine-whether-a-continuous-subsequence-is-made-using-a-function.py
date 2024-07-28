def inner(a, b, n1, n2):
    for i in range(a-b+1):
        if n1[i] == n2[0]:
            if n1[i:i+b] == n2:
                return 'Yes'
    return 'No'

a, b = map(int, input().split())
n1 = list(input().split())
n2 = list(input().split())

print(inner(a, b, n1, n2))