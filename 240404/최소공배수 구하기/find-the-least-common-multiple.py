def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())
num = gcd(n, m)
c, d = (n // num), (m // num)
print(num*c*d)