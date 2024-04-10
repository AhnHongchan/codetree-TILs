n = int(input())
ans = ''
while True:
    if n < 2:
        ans += str(n)
        break
    else:
        x = n % 2
        ans += str(x)
        n //= 2

print(ans[::-1])