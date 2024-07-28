def month(M):
    if M <= 12 and M>=1:
        return True
    return False

def year_2021(M, D):
    if month(M):
        if M in [1, 3, 5, 7, 8, 10, 12]:
            if D <= 31:
                return 'Yes'
        elif M == 2:
            if D <= 28:
                return 'Yes'
        else:
            if D <= 30:
                return 'Yes'
    return 'No'

a, b = map(int, input().split())
print(year_2021(a, b))