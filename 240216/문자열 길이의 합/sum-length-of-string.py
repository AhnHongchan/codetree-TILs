n = int(input())
cnt = 0
txt_sum = 0
for i in range(n):
    txt = input()
    if txt[0] == 'a':
        cnt += 1
    txt_sum += len(txt)

print(txt_sum, cnt)