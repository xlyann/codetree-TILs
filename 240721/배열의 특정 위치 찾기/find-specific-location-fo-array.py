a = list(map(int, input().split()))
print(sum(a[1::2]), f'{sum(a[2::3])/3:.1f}')