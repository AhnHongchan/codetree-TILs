txt = list(input())
a = txt[0]
b = txt[1]
for i in range(len(txt)):
    if txt[i] == a:
        txt[i] = b
    elif txt[i] == b:
        txt[i] = a

print(*txt, sep='')