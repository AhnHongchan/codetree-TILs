txt = input()
char = input()

for i in range(len(txt)):
    if char[:] == txt[i:i+len(char)]:
        print(i)
else:
    print(-1)