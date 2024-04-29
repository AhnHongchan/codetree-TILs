n, m = map(int, input().split())

Arr = [0] * 1000001
Brr = [0] * 1000001

idx_a = 0
cnt_a = 0
for k in range(n):
    t, d = input().split()
    for i in range(int(t)):
        if d == 'L':
            idx_a -= 1
            cnt_a += 1
            Arr[cnt_a] = idx_a
        else:
            idx_a += 1
            cnt_a += 1
            Arr[cnt_a] = idx_a

    if k == n-1:
        for j in range(cnt_a+1, 1000001):
            Arr[j] = idx_a

idx_b = 0
cnt_b = 0
for k in range(m):
    t, d = input().split()
    for i in range(int(t)):
        if d == 'L':
            idx_b -= 1
            cnt_b += 1
            Brr[cnt_b] = idx_b
        else:
            idx_b += 1
            cnt_b += 1
            Brr[cnt_b] = idx_b

    if k == m-1:
        for j in range(cnt_b+1, 1000001):
            Brr[j] = idx_b

ans = 0
for i in range(1, 1000001):
    if Arr[i] == Brr[i]:
        if Arr[i-1] != Brr[i-1]:
            ans += 1

print(ans)