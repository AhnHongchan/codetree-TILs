N = int(input())
arr = [int(input()) for _ in range(N)]

max_cnt = 0
cnt = 0
for i in range(N):
    if i >= 1 and arr[i] * arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)