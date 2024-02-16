txt = input()
char = input()

cnt = 0
for i in range(len(txt)):
    if char == txt[i:i+len(char)]:
        cnt += 1

print(cnt)