txt = input()
n = int(input())

if len(txt) > n:
    for x in txt[len(txt)-1:len(txt)-1-n:-1]:
        print(x, end='')
else:
    for y in txt[::-1]:
        print(y, end='')