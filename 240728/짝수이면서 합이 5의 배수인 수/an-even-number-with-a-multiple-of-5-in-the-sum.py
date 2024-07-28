def f(num):
    if num % 2 == 0 and (num//10 + num %10)%5 == 0:
        return 'Yes'
    else:
        return 'No'

a = int(input())
print(f(a))