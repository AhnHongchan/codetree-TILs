n, h ,t = map(int, input().split())
h_list = list(map(int, input().split()))

ans = 100000000
for i in range(n-t):
    cnt = 0
    for j in range(t):
        x = h_list[i+j]
        cnt += abs(x-h)
    if ans > cnt:
        ans = cnt

print(ans)