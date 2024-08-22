save = []

def command(a, b=0):
    if a == 'push_back':
        save.append(int(b))
    if a == 'get':
        print(save[int(b)-1])
    if a == 'size':
        print(len(save))
    if a == 'pop_back':
        save.pop()

n = int(input())
for i in range(n):
    a = list(input().split())
    command(*a)