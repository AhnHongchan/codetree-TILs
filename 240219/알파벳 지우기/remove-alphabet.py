txt1 = input()
txt2 = input()

str1 = ''
str2 = ''
for x in txt1:
    if '0' <= x <= '9':
        str1 += x
    else:
        pass

for y in txt2:
    if '0' <= y <= '9':
        str2 += y
    else:
        pass

print(int(str1) + int(str2))