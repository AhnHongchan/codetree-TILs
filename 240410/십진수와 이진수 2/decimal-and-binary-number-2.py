N = input()
n = len(N)
ans = 0
for i in range(n):
    ans += int(N[n-1-i]) * (2 ** i)

ans *= 17
cnt = ''
while True:
    if ans < 2:
        cnt += str(ans)
        print(cnt[::-1])
        break
    else:
        x = ans % 2
        cnt += str(x)
        ans //= 2