def find(string):
    global target
    for i in range(len(target)-len(string)+1):
        if target[i] == string[0]:
            if target[i:i+len(string)] == string:
                return i
    return -1

target = input()
string = input()
print(find(string))