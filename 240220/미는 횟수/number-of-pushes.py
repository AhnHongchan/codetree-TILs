txt1 = input()
txt2 = input()


for i in range(1, len(txt1)):
    txt1 = txt1[-1] + txt1[:-1]
    if txt1 == txt2:
        print(i)
        break
    else:
        pass
else:
    print(-1)