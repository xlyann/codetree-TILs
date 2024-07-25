string = input()
start = string[0]
count = 0
RLE = ''
for i in range(len(string)):
    if start != string[i]:
        RLE += str(start)
        RLE += str(count)
        start = string[i]
        count = 1
    else:
        count += 1
    if i == len(string)-1:
        RLE += str(start)
        RLE += str(count)

print(len(RLE))
print(RLE)