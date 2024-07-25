a = input()
length = int(input())
if length > len(a):
    print(a[::-1])
else:
    print(a[-1:-length-1:-1])