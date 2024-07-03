s, e = map(int, input().split())
numbers = [i for i in range(s, e+1)]

ans = 0
for x in numbers:
    num = 0
    while x:
        num += x % 10
        x //= 10
    ans = max(ans, num)

print(ans)