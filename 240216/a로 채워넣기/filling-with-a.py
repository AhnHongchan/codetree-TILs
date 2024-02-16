txt = input()
txt = txt[0] + 'a' + txt[2:len(txt)-2] + 'a' + txt[len(txt)-1]
print(txt)