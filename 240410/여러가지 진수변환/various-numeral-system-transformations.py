n, b = map(int, input().split())
ans = ''
while True:
    if n < b:
        ans += str(n)
        break
    else:
        x = n % b
        ans += str(x)
        n //= b

print(ans[::-1])