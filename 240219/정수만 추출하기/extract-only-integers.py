a, b = input().split()
str1 = ''
for x in a:
    if '0' <= x <= '9':
        str1 += x
    else:
        break

str2 = ''

for y in b:
    if '0' <= y <= '9':
        str2 += y
    else:
        break

print(int(str1)+int(str2))