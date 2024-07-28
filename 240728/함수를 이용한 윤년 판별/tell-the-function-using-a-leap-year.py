def yun_year(num):
    if num%4 == 0:
        if num%100 == 0 and num%400 != 0:
            return 'false'
        return 'true'
    return 'false'

a = int(input())
print(yun_year(a))