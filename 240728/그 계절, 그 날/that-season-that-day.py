def yun_year(Y):
    if Y%4 != 0:
        return False
    if Y%100 != 0:
        return True
    if Y%400 == 0:
        return True
    return False

def month(Y, M):
    if yun_year(Y) and M == 2:
        return 29
    if M == 2:
        return 28
    if M in [4, 6, 9, 11]:
        return 30
    return 31

def day_true(Y, M, D):
    if M <= 12 and D <= month(Y, M):
        return True
    return False

def season(M):
    if 3<= M and M<=5:
        print('Spring')
    elif 6<= M and M<=8:
        print('Summer')
    elif 9<= M and M<=11:
        print('Fall')
    else:
        print('Winter')
    
Y, M, D = map(int, input().split())
if day_true(Y, M, D):
    season(M)
else:
    print(-1)