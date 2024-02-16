lst = []
for i in range(3):
    txt = input()
    length = len(txt)
    lst.append(length)

min_v = 100

for i in range(3):
    if min_v > lst[i]:
        min_v = lst[i]

print(min_v)