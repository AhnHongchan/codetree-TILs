txt = input()
for i in range(len(txt)-1, -1, -1):
    if i % 2 == 1:
        print(txt[i], end = '')