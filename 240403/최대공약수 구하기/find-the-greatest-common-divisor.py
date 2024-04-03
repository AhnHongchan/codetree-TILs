def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m =map(int, input().split())
result = gcd(n, m)
print(result)