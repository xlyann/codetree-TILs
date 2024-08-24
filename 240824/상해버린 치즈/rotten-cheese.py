people, cheese, record, sick_record = map(int, input().split())
eat = list(tuple(map(int, input().split())) for _ in range(record))
sick = list(tuple(map(int, input().split())) for _ in range(sick_record))

ans = 0
for i in range(record):
    pacient = [0]*(people+1)
    stomach = [0]*(people+1)
    guess = True
    for who, num, second in eat:
        if i == num and pacient[who] == 0:
            pacient[who] = 1
            stomach[who] = second+1
    for who_sick, sick_time in sick:
        if pacient[who_sick] == 1 and stomach[who_sick] <= sick_time:
            continue
        guess = False
        break
    if guess:
        ans = max(ans, pacient.count(1))
print(ans)