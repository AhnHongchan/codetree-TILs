txt = input()

cnt1 = 0
cnt2 = 0
for i in range(len(txt)-1):
    if 'ee' in (txt[i]+txt[i+1]):
        cnt1 += 1
    if 'eb' in (txt[i]+txt[i+1]):
        cnt2 += 1

print(cnt1, cnt2)