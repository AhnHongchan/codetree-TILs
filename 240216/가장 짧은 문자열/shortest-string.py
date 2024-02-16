lst = []

for i in range(3):
    txt = input()
    length = len(txt)
    lst.append(length)

lst.sort()

print(f'{lst[2] - lst[0]}')