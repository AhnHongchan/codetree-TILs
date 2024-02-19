txt, b = input().split()
for i in range(int(b)):
    num = int(input())
    if num == 1:
        txt = txt[1:] + txt[0]
    elif num == 2:
        txt = txt[-1] + txt[:-1]
    else:
        txt = txt[::-1]
    print(txt)