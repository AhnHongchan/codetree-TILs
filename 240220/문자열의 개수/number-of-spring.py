cnt = 0
lst = []
while True:
    txt = input()
    if txt == '0':
        break
    cnt += 1
    if cnt % 2 == 1:
        lst.append(txt)

print(cnt)
for x in lst:
    print(x)