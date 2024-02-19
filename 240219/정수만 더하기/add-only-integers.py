txt = input()
sum = 0
for elem in txt:
    if '0' <= elem <= '9':
        sum += int(elem)

print(sum)