a = input()
new = list(a)
first = new[0]
second = new[1]

for i in range(len(a)):
    if new[i] == first:
        new[i] = second
    elif new[i] == second:
        new[i] = first

print(''.join(new))