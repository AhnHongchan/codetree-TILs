txt = []
for i in range(10):
    txt.append(input())

char = input()
cnt = 0

for i in range(10):
    if txt[i][-1] == char:
        print(txt[i])
        cnt += 1

if cnt == 0:
    print('None')