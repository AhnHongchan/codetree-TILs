max_cnt = 0
cnt = 0
lst = []
N = int(input())
for _ in range(N):
    num = int(input())
    if lst:
        if lst[-1] != num:
            lst = []
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0

    lst.append(num)
    cnt += 1

print(max_cnt)