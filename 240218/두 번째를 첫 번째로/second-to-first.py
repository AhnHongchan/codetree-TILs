txt = input()
txt = list(txt)
val = txt[1]
for i in range(len(txt)):
    if txt[i] == val:
        txt[i] = txt[0]

print(''.join(txt))