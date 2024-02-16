lst = []

for i in range(3):
    txt = input()
    length = len(txt)
    lst.append(length)

for i in range(2):
    for j in range(i+1, 3):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst[2] - lst[0])