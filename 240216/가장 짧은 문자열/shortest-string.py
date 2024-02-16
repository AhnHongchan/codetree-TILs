lst = []

for i in range(3):
    txt = input()
    length = len(txt)
    lst.append(length)

for i in range(2):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst[2] - lst[0])