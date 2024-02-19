txt = input()
print(txt)

for i in range(len(txt)):
    txt = txt[-1] + txt[:-1]
    print(txt)