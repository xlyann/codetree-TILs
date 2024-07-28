def palindrome(string):
    for i in range(len(string)//2+1):
        if string[i] != string[-i-1]:
            return 'No'
    return 'Yes'

a = input()
print(palindrome(a))