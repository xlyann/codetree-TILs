N, M, K = map(int, input().split())
fine = [-1] + [K]*N
cnt = [int(input()) for _ in range(M)]

student = -1

for i in cnt:
    fine[i] -= 1
    if fine.count(0) > 0:
        student = fine.index(0)
        break

print(student)