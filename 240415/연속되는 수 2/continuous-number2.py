max_cnt = 1
cnt = 1
lst = []
N = int(input())
for _ in range(N):
    num = int(input())
    lst.append(num)

for i in range(N-1):
    if lst[i] == lst[i+1]:
        cnt += 1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)