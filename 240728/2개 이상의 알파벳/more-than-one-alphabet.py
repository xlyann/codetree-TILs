def alpha_1(string):
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            return 'Yes'
    return 'No'

a = input()
print(alpha_1(a))