txt = input()
alpha = input()

cnt = 0
for x in txt:
    if alpha == x:
        cnt += 1

print(cnt)