string = input()
save = input()
while save in string:
    cut = string.find(save)
    string = string[:cut] + string[cut+len(save):]
print(string)