N, M = map(int, input().split())

arr = [0] * 1001
brr = [0] * 1001

cnt = 0
for i in range(N):
    v,t = map(int, input().split())
    for j in range(t):
        cnt += 1
        arr[cnt] = arr[cnt-1]+v
    if i == N-1:
        for k in range(cnt+1, 1001):
            arr[k] = arr[k-1]

cnt = 0
for i in range(M):
    v,t = map(int, input().split())
    for j in range(t):
        cnt += 1
        brr[cnt] = brr[cnt-1]+v
    if i == M-1:
        for k in range(cnt+1, 1001):
            brr[k] = brr[k-1]

ans = 1
for i in range(2, 1001):
    if arr[i] == brr[i]:
        if arr[i-1] != brr[i-1]:
            ans += 1
    elif arr[i] > brr[i]:
        if arr[i-1] <= brr[i-1]:
            ans += 1
    elif arr[i] < brr[i]:
        if arr[i-1] >= brr[i-1]:
            ans += 1

print(ans)