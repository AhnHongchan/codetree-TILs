txt = input()
n = int(input())

for x in txt[len(txt)-1:len(txt)-1-n:-1]:
    print(x, end='')