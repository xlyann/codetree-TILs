_list = list(input())

limit = len(_list)

cnt = 0

for i in range(limit):
    for j in range(i+2, limit-1):
        if _list[i]+_list[i+1]+_list[j]+_list[j+1] == '(())':
            cnt += 1

print(cnt)