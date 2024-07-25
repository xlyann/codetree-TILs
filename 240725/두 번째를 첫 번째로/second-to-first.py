string = list(input())
save = string[1]
for i in range(len(string)):
    if string[i] == save:
        string[i] = string[0]
print(''.join(string))