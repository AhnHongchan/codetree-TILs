txt = []
for i in range(10):
    txt.append(input())

char = input()

for i in range(10):
    if txt[i][-1] == char:
        print(txt[i])