a, b = map(int, input().split())
num = input()
n = len(num)

ans = 0
for i in range(n):
    ans += int(num[n-1-i]) * (a ** i)

cnt = ''
while True:
    if ans < b:
        cnt += str(ans)
        print(cnt[::-1])
        break
    else:
        x = ans % b
        cnt += str(x)
        ans //= b